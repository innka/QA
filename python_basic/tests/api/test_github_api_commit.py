import pytest

@pytest.mark.idv_project4
def test_list_commits(github_api_commit):
    r = github_api_commit.get_list_commits("innka","QA")
    #print(len(commit))
    assert len(r) !=0
    assert len(r) == 8
    assert r[0]["sha"] == "21b8d5bcaaffc98014afb0a5a6bb7729b374bb7a"
    assert r[1]["sha"] == "8bb90eb2d8f0c3c00a1ea59ebd4a000b0eb6396e"
    assert r[7]["sha"] == "cefc3c68ff37b8909adfa63ac51c850776fbc76c"

@pytest.mark.idv_project4
def test_get_commits(github_api_commit):
    r = github_api_commit.get_commit("innka","QA", "21b8d5bcaaffc98014afb0a5a6bb7729b374bb7a")
    assert r["sha"] == "21b8d5bcaaffc98014afb0a5a6bb7729b374bb7a"
    assert r["commit"]["message"] == "modul 19 UI Testing"

@pytest.mark.idv_project4
def test_get_commit_status(github_api_commit):
    r = github_api_commit.get_commit_status("innka","QA","21b8d5bcaaffc98014afb0a5a6bb7729b374bb7a")
    assert r["state"] == "pending"

@pytest.mark.idv_project4
def test_get_list_commit_comments_repo(github_api_commit):
     r = github_api_commit.get_list_commit_coments_repo("innka","QA")
     assert len(r) == 0


@pytest.mark.idv_project4
def test_get_commit_coment(github_api_commit):
    r = github_api_commit.get_commit_coment("innka","QA",0)
    assert r["message"] == "Not Found"
    assert r["status"] == "404"