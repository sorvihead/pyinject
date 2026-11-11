# fmt: off
from tests.typing.composition.positive import Application
from tests.typing.models import Repository
from tests.typing.wiring.positive import async_process, process

from pyinject import Provide, Provider

process()  # E: mypy=call-arg pyright=reportCallIssue
process("item", service=1)  # E: mypy=arg-type pyright=reportArgumentType
process(1)  # E: mypy=arg-type pyright=reportArgumentType
wrong: Repository = Provide[Application.service]  # E: mypy=assignment pyright=reportAssignmentType
Provider[Application.service](1)  # E: mypy=call-arg pyright=reportCallIssue
Provide[42]  # E: mypy=call-overload pyright=reportArgumentType,reportCallIssue
Application().wire(modules=["not-a-module"])  # E: mypy=list-item pyright=reportArgumentType
# A coroutine is not the awaited result.
repo: Repository = async_process("item")  # E: mypy=assignment pyright=reportAssignmentType
# fmt: on
