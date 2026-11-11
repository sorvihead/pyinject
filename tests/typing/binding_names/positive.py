from typing import assert_type

from pyinject import providers


def required(*, kwargs: bytes) -> int:
    return len(kwargs)


def optional(*, kwargs: bytes = b"") -> int:
    return len(kwargs)


def ordinary(value: int) -> int:
    return value


def all_names(*, factory: str, self: int, args: bool, kwargs: bytes) -> str:
    return f"{factory}: {self} {args} {kwargs!r}"


class NamedConstructor:
    def __init__(self, *, kwargs: bytes = b"") -> None:
        self.value = kwargs


assert_type(providers.Factory(required, kwargs=b"x").ref, int)
assert_type(providers.Singleton(required, kwargs=b"x").ref, int)
assert_type(providers.Factory(optional, kwargs=b"x").ref, int)
assert_type(providers.Singleton(optional, kwargs=b"x").ref, int)
assert_type(providers.Factory(NamedConstructor, kwargs=b"x").ref, NamedConstructor)
assert_type(providers.Singleton(NamedConstructor, kwargs=b"x").ref, NamedConstructor)
assert_type(providers.Factory(all_names, factory="x", self=1, args=True, kwargs=b"x").ref, str)
