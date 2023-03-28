from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Size(BaseModel):
    name: str


Sizes = [Size(name='Small'), Size(name='Medium'), Size(name='Big')]


@app.get('/API/sizes')
def sizes() -> list[str]:
    return [s.name for s in Sizes]
