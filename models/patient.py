from pydantic import BaseModel
from datetime import datetime

# mcq question answer model


class Patient(BaseModel):
    name: str
    age: str
    gender: str
    blood_group: str
    weight: str
