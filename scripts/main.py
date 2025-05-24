from typing import Union
#union allows variables to be of multiple types
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#BaseModel is a class from pydantic
#it defines the structure of input data 
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None]=None
# Input Data expected by FastAPI
# {
#   "name": "Book",
#   "price": 10.5,
#   "is_offer": true
# }

@app.get("/") #creates a GET endpoint at / (root path)
def read_root():
    #returns the below message as a json response when accessed
    return {"Hello":"World"}


@app.get("/items/{item_id}") # defines a GET endpoint at /items/{item_id}?q=value
#here the q is optional
def read_item(item_id: int, q: Union[str, None] = None):
    #item_id is required path parameter
    #q is optional query parameter
    return {"item_id":item_id, "q":q} #returns both parameters as JSON

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name":item.name, "item_id":item_id}