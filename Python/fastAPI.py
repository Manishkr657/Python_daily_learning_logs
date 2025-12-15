# FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
# It is built on top of Starlette for the web parts and Pydantic for the data parts.

# Installation pip install "fastapi[standard]"

from typing import Union
from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}