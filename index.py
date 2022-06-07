from fastapi import FastAPI
from routes.patient import patient

#shivus comment

app = FastAPI()
app.include_router(patient)
