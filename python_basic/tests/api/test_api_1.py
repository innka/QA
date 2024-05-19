import pytest

@pytest.mark.change #група тестів
def test_remove_name(user):
    user.name = ""
    assert user.name == ""

@pytest.mark.check   
def test_name(user):
    assert user.name == "Ivan"
    
@pytest.mark.check   
def test_second_name(user):
    assert user.second_name == "Franco"
    
