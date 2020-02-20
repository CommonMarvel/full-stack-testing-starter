import json

import pytest
import urllib3


# Test 3A (arrange, act, assert)
@pytest.mark.parametrize("env", ["dev"])
def test_get(setup_function, env):
    # get config from setup function (arrange)
    config = setup_function

    # get HTTP utility (arrange)
    http = urllib3.PoolManager()

    # invoke HTTP GET request (act)
    resp = http.request(method="GET",
                        headers={
                            "accept": "application/json",
                        },
                        url="{}".format(
                            config["demo"][env]["api"]["host"] + config["demo"][env]["api"]["path"]["get"],
                        ),
                        fields={
                            "name": "Vincent"
                        })

    # get response (act)
    body = json.loads(resp.data.decode("utf-8"))

    # assert
    assert resp.status == 200 and body["args"]["name"] == "Vincent"
