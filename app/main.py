from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello My": "Fantastic Test speed is this faster World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/category/{category_id}")
def read_category(category_id: int, q: Union[str, None] = None):
    return {"category_id": category_id, "q": q}
