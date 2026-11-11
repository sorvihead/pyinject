from typing import assert_type


def identity(value: int) -> int:
    return value


assert_type(identity(1), int)
