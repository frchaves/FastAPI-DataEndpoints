import uvicorn
from fastapi import FastAPI, Query, Body
from datetime import datetime
from dateutil import parser
from pydantic import BaseModel, ValidationError
from db import Payload, Reading, fake_items_db, fake_items_db_2


app = FastAPI(title="ChallengeApp")


@app.post("/data")
def post_data(body: str = Body(..., media_type='text/plain')):
    lines = body.split("\n")
    for line in lines:
        values = line.split(" ")
        reading_line = {"time": values[0], "name": values[1], "value": values[2]}
        try:
            reading = Reading(**reading_line)
        except ValidationError:
            return {"success": False}
        fake_items_db_2.append(reading)

    return {"success": True}


@app.get('/data')
def get_data(_from: datetime = Query(..., alias="from"), to: datetime = Query(..., alias="to")):
    date_range = []
    for data in fake_items_db:
        time = parser.parse(data['time'])
        if time >= _from and time <= to:
            date_range.append(data)

    return date_range


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

