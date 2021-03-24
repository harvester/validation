from .common import *

if_harvester = pytest.mark.skipif(not CATTLE_TEST_URL, reason="Harvester SERVER not provided")

@if_harvester
def test_login():
    url = CATTLE_TEST_URL.strip('/') + HARVESTER_LOGIN_URL
    r = requests.post(url, json={
        'username': ADMIN_USER,
        'password': ADMIN_PASSWORD,
        'responseType': 'json'
    }, verify=False)

    assert r.status_code == 200