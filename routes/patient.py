from fastapi import APIRouter
from config.db import conn
from models.patient import Patient
from schemas.patient import serializeDict, serializeList
from bson import ObjectId


patient = APIRouter()


@patient.post("/patient/", tags=["Patient"])
async def insert_patient(patient: Patient):
    conn.patientdb.patient.insert_one(dict(Patient))
    return serializeList(conn.patientdb.patient.find())


@patient.get("/patient/", tags=["Patient"])
async def get_all_patient():
    return serializeList(conn.patientdb.patient.find())


@patient.get("/patient/{id}", tags=["Patient"])
async def get_one_patient(id):
    return serializeDict(conn.patientdb.patient.find_one({"_id": ObjectId(id)}))


@patient.put("/patient/{id}", tags=["Patient"])
async def update_patient(id, patient: Patient):
    conn.patientdb.patient.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(Patient)}
    )
    return serializeDict(conn.patientdb.patient.find_one({"_id": ObjectId(id)}))


@patient.delete("/patient/{id}", tags=["Patient"])
async def delete_patient(id):
    return serializeDict(
        conn.patientdb.patient.find_one_and_delete({"_id": ObjectId(id)})
    )
