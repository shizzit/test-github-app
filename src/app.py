from typing import Union
from fastapi import FastAPI

from .github.api import get_token, workflow_dispatch

app = FastAPI()

@app.get("/")
def root():
    token = get_token()
    response_status = workflow_dispatch(token)
    return {"response":f"{response_status}"}

@app.get("/health")
def health():
    return {"healthy":"true"}
