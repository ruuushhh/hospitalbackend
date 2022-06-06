from fastapi import FastAPI
from config.db import conn
from models.patient import Patient
from schemas.patient import serializeDict, serializeList


app = FastAPI()


@app.post("/patient/", tags=["Patient"])
async def insert_patient(patient: Patient):
    conn.patientdb.patient.insert_one(dict(Patient))
    return serializeList(conn.patientdb.patient.find())


@app.get("/patient/", tags=["Patient"])
async def get_all_patient():
    return serializeList(conn.patientdb.patient.find())


@app.get("/patient/{id}", tags=["Patient"])
async def get_one_patient(id):
    return serializeDict(conn.patientdb.patient.find_one({"_id": ObjectId(id)}))


@app.put("/patient/{id}", tags=["Patient"])
async def update_patient(id, patient: Patient):
    conn.patientdb.patient.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(Patient)}
    )
    return serializeDict(conn.patientdb.patient.find_one({"_id": ObjectId(id)}))


@app.delete("/patient/{id}", tags=["Patient"])
async def delete_patient(id):
    return serializeDict(
        conn.patientdb.patient.find_one_and_delete({"_id": ObjectId(id)})
    )
