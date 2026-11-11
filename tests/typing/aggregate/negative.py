# fmt: off
from tests.typing.aggregate.positive import Application
from tests.typing.models import Repository, Service

from pyinject import providers

repo = Repository("memory:")
providers.FactoryAggregate[Service]( bad=providers.Factory(Repository, "memory:") )  # E: mypy=arg-type pyright=reportArgumentType
providers.FactoryAggregate[Service]( bad=providers.Singleton(Service, repo) )  # E: mypy=arg-type pyright=reportArgumentType
providers.Factory(Service, repo=Application.service.ref)  # E: mypy=arg-type pyright=reportArgumentType
Application().service()  # E: mypy=call-arg pyright=reportCallIssue
Application().service(1)  # E: mypy=arg-type pyright=reportArgumentType
Application().service("primary", repo=repo)  # E: mypy=call-arg pyright=reportCallIssue
value: Service = Application.service.ref  # E: mypy=assignment pyright=reportAssignmentType
# fmt: on
