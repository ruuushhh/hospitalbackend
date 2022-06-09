from pydantic import BaseModel
from datetime import datetime

# mcq question answer model


class Doctor(BaseModel):
    name: str
    age: str
    gender: str
    profession: str