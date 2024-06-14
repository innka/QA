import pytest

@pytest.mark.idv_project4
def test_get_emoji(github_api_emoji):
    r = github_api_emoji.get_emogi()
    assert len(r) == 1935
    assert r["+1"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f44d.png?v8"
    assert r["cat"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f431.png?v8"
    assert r["ukraine"] == "https://github.githubassets.com/images/icons/emoji/unicode/1f1fa-1f1e6.png?v8"

    