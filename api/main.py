from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def root():
    return {'msg': "Hello from API 1."}


@app.get('/from2')
def from2():
    response = requests.get("http://api2:8001")
    print(response.json())
    return response.json()
