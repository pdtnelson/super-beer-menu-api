from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/beers")
def get_beers():
    return [
        {"name": "Jubleale", "desc": "Robbie's tasty ass beer"},
        {"name": "Torpedo", "desc": "Tastes kinda old right now"}
    ]
