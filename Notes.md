# Instructions

- Create `main.py`
    - `touch main.py`
    - Open file using terminal `code main.py`
- Then we will run the fastapi using a uvicorn server
    - To do this do `pip install unvicorn`
    - Then `uvicorn main:app --reload`
    - Since we are running now on codespaces, we can query it by passing `items` and `q` information like this `https://scaling-fishstick-wjv4r454x4rh9x97-8000.app.github.dev/items/6?q=apple`
    - There is interactive docs in FastAPI that can be used by `https://scaling-fishstick-wjv4r454x4rh9x97-8000.app.github.dev/docs`
    - Documentation by redoct `https://scaling-fishstick-wjv4r454x4rh9x97-8000.app.github.dev/redoc`

- `from pydantic import BaseModel`
    - `BaseModel` is a class from Pydantic, used in FastAPI to define and validate request bodies.
    - You create a class that inherits from `BaseModel` to define the structure of input data your API expects.






