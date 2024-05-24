import pytest
import requests

@pytest.mark.http
def test_first_request():
    r = requests.get('http://api.github.com/zen')
    print(r.text)

@pytest.mark.http
def test_second_request():
    r = requests.get('https://api.github.com/users/defunkt')
    #print(f"Reponse is {r.text}") #- вивід всього
    
    #print(f"Response Body is {r.json()}/n")
    body = r.json()
    assert body['name'] == "Chris Wanstrath"

    #print(f"Response Status code is {r.status_code}/n")
    assert r.status_code == 200
    
    #print(f"Response Headers are {r.headers}")
    headers = r.headers
    assert headers['Server'] == 'GitHub.com'

@pytest.mark.http
def test_status_request():
    r = requests.get('https://api.github.com/users/sergii_butenko')
    assert r.status_code == 404