import requests

def test_AnyName():
    r=requests.get("https://www.google.com/")
    assert 200==r.status_code, "has to bee 200"
