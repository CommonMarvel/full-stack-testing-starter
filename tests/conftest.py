import json

import pytest


@pytest.fixture(scope="session")
def setup_function(request):
    with open("config.json") as configJson:
        config = json.load(configJson)

    def teardown_function():
        print()

    request.addfinalizer(teardown_function)

    return config
