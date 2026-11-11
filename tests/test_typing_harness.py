from collections import Counter

import pytest
from scripts.check_typing import Diagnostic, verify_diagnostics


@pytest.mark.parametrize(
    "actual",
    [
        [],
        [("x.py", 2, "assignment")],
        [("x.py", 1, "arg-type")],
        [("other.py", 1, "assignment")],
        [("x.py", 1, "assignment"), ("x.py", 1, "assignment")],
    ],
)
def test_missing_extra_or_misplaced_diagnostic_fails(actual: list[Diagnostic]) -> None:
    with pytest.raises(AssertionError):
        verify_diagnostics(Counter({("x.py", 1, "assignment"): 1}), Counter(actual))


def test_exact_diagnostic_passes() -> None:
    verify_diagnostics(Counter({("x.py", 1, "assignment"): 1}), Counter({("x.py", 1, "assignment"): 1}))
