import os, sys, pytest

from fastapi.testclient import TestClient
from main import app
client = TestClient(app)


test_get_data = {
    "from": "2022-04-14T13:10:17.000Z",
    "to": "2022-04-17T13:10:17.000Z"
}

with open(os.path.join(sys.path[0], "test_data.txt"), "r") as f:
    test_post_data = f.read()


def test_get_main():
    response = client.get("/data", params=test_get_data)
    assert response.json() == [
    {
        "time": "2022-04-14T13:10:17.000Z",
        "name": "Voltage",
        "value": 1.34
    },
    {
        "time": "2022-04-15T13:10:17.000Z",
        "name": "Current",
        "value": 19
    },
    {
        "time": "2022-04-17T13:10:17.000Z",
        "name": "Current",
        "value": 14
    }
]
