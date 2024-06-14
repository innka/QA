import pytest
from modules.api.clients.github_user_search import GitHub
from modules.api.clients.github_commit import GitHubCommit
from modules.api.clients.github_emoji import GitHubEmoji

class User:

    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Ivan"
        self.second_name = "Franco"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()
    yield api

@pytest.fixture
def github_api_commit():
    api = GitHubCommit()
    yield api

@pytest.fixture
def github_api_emoji():
    api = GitHubEmoji()
    yield api
