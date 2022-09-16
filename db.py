from pydantic import BaseModel


class Payload(BaseModel):
    data: str = ""


class Reading(BaseModel):
    time: str
    name: str
    value: float

# This is a fake database which stores data in-memory while the process is running
# Feel free to change the data structure to anything else you would like
# database: dict[str, Reading] = {}

fake_items_db = [
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

fake_items_db_2 = []