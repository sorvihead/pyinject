from tests.typing.models import Repository, Service, make_service

from pyinject import providers

repo = providers.Singleton(Repository, "memory:")
providers.Factory(Service, repo=42)  # E: mypy=arg-type pyright=reportArgumentType
providers.Factory(Service, typo=repo.ref)  # E: mypy=call-arg pyright=reportCallIssue,reportCallIssue
providers.Factory(Service)  # E: mypy=call-arg pyright=reportCallIssue
providers.Singleton(Repository, dsn=1)  # E: mypy=arg-type pyright=reportArgumentType
providers.Factory(make_service, repo=repo.ref)  # E: mypy=call-arg pyright=reportCallIssue
providers.Factory(make_service, repo.ref, True)  # E: mypy=call-arg pyright=reportCallIssue
