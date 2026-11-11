class Repository:
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn


class Service:
    def __init__(self, repo: Repository) -> None:
        self.repo = repo


class OtherService(Service):
    pass


def make_service(repo: Repository, /, *, enabled: bool = True) -> Service:
    return Service(repo)
