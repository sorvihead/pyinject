# fmt: off
from tests.typing.containers.positive import Application

Application().service(1)  # E: mypy=call-arg pyright=reportCallIssue
Application().service(repo=None)  # E: mypy=call-arg pyright=reportCallIssue
Application.service()  # E: mypy=operator pyright=reportCallIssue
Application(unknown=1)  # E: mypy=call-arg pyright=reportCallIssue


class SubApplication(Application):  # E: mypy=misc pyright=reportGeneralTypeIssues
    pass
# fmt: on
