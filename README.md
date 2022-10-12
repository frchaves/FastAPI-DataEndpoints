### Description:
An API for storing and getting electric readings from IoT devices.


### Tech Stack:
- FastAPI

### Setup:
- Clone the project to a folder (_**git clone https://github.com/frchaves/FastAPI-DataEndpoints.git**_)
- Open the terminal in the project folder
- Run the application with:
  - uvicorn main:app --reload
  - Test the endpoints at (_**http://localhost:8001/docs#**_)
  or with
 ``` -curl --request POST --url http://localhost:8001/data -d '{"data":"1649941817 Voltage 1.34 1649941818 Voltage 1.35 1649941817 Current 12.0 1649941818 Current 14.0"}'
 ```
