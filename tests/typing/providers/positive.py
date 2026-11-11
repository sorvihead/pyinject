from typing import assert_type

from tests.typing.models import Repository, Service, make_service

from pyinject import providers

repo = providers.Singleton(Repository, dsn="memory:")
service = providers.Factory(Service, repo=repo.ref)
function = providers.Factory(make_service, repo.ref, enabled=True)
assert_type(repo.ref, Repository)
assert_type(service.ref, Service)
assert_type(function.ref, Service)
assert_type(service, providers.Factory[Service])

# Deliberate unsound boundary: accepted statically, not valid outside the DSL.
ordinary_service = Service(repo=repo.ref)
assert_type(ordinary_service, Service)


class Builder:
    def __call__(self, *, repo: Repository) -> Service:
        return Service(repo)

    def build(self, repo: Repository) -> Service:
        return Service(repo)


assert_type(providers.Factory(Builder(), repo=repo.ref).ref, Service)
assert_type(providers.Factory(Builder().build, repo.ref).ref, Service)
