"""Run both checkers and match every diagnostic by file, line and code."""

import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

type Diagnostic = tuple[str, int, str]
ROOT = Path(__file__).resolve().parents[1]


def verify_diagnostics(expected: Counter[Diagnostic], actual: Counter[Diagnostic]) -> None:
    if expected != actual:
        raise AssertionError(f"missing: {expected - actual}\nunexpected: {actual - expected}")


def expected_diagnostics(files: list[Path], checker: str) -> Counter[Diagnostic]:
    expected: Counter[Diagnostic] = Counter()
    for file in files:
        for line, text in enumerate(file.read_text().splitlines(), 1):
            marker = re.search(rf"\b{checker}=([\w,-]+)", text)
            if marker:
                for code in marker[1].split(","):
                    if code != "none":
                        expected[(file.relative_to(ROOT).as_posix(), line, code)] += 1
    return expected


def run(checker: str, files: list[Path]) -> None:
    paths = [str(file.relative_to(ROOT)) for file in files]
    command = [sys.executable, "-m", checker]
    command += ["--show-column-numbers", "--no-error-summary", "--no-pretty"] if checker == "mypy" else ["--outputjson"]
    result = subprocess.run(command + paths, cwd=ROOT, capture_output=True, text=True, check=False)
    actual: Counter[Diagnostic] = Counter()
    if checker == "mypy":
        for line in result.stdout.splitlines():
            match = re.fullmatch(r"(.+?):(\d+):\d+: error: .*  \[([^]]+)\]", line)
            if match:
                actual[(Path(match[1]).as_posix(), int(match[2]), match[3])] += 1
            elif line and ": note:" not in line:
                raise AssertionError(f"unparsed mypy output: {line}")
    else:
        payload = json.loads(result.stdout)
        for item in payload["generalDiagnostics"]:
            actual[
                (
                    Path(item["file"]).relative_to(ROOT).as_posix(),
                    item["range"]["start"]["line"] + 1,
                    item.get("rule", "unknown"),
                )
            ] += 1
    if result.stderr or result.returncode not in (0, 1):
        raise AssertionError(f"{checker} failed ({result.returncode}): {result.stderr}\n{result.stdout}")
    if (result.returncode == 0) != (not actual):
        raise AssertionError(f"{checker}: exit status inconsistent with diagnostics")
    verify_diagnostics(expected_diagnostics(files, checker), actual)
    print(f"{checker}: {len(files)} files, {sum(actual.values())} expected diagnostics matched")


def main() -> None:
    files = sorted((ROOT / "tests/typing").rglob("*.py")) + sorted((ROOT / "examples").glob("*.py"))
    if not files:
        raise AssertionError("no typing fixtures found")
    for checker in ("mypy", "pyright"):
        run(checker, files)


if __name__ == "__main__":
    main()
