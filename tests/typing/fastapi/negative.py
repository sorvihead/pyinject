# fmt: off
from tests.typing.composition.positive import Application
from tests.typing.fastapi.positive import async_endpoint, endpoint
from tests.typing.models import Repository

from pyinject import Provider

endpoint()  # E: mypy=call-arg pyright=reportCallIssue
endpoint(Repository("memory:"))  # E: mypy=arg-type pyright=reportArgumentType
wrong: Repository = Provider[Application.service]()  # E: mypy=assignment pyright=reportAssignmentType
async_endpoint()  # E: mypy=call-arg,unused-coroutine pyright=reportCallIssue
# fmt: on
