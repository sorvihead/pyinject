from collections.abc import Callable
from typing import overload

from . import providers

class _CallableMarker[T]:
    def __call__(self) -> T: ...

class _Provide:
    @overload
    def __getitem__[T](self, provider: providers.Provider[T], /) -> T: ...
    @overload
    def __getitem__[T](self, provider: providers.FactoryAggregate[T], /) -> Callable[[str], T]: ...

class _Provider:
    @overload
    def __getitem__[T](self, provider: providers.Provider[T], /) -> _CallableMarker[T]: ...
    @overload
    def __getitem__[T](self, provider: providers.FactoryAggregate[T], /) -> _CallableMarker[Callable[[str], T]]: ...

Provide: _Provide
Provider: _Provider

def inject[**P, R](function: Callable[P, R], /) -> Callable[P, R]: ...
