from fastapi import APIRouter
from config.db import conn
from models.doctor import Doctor
from schemas.patient import serializeDict, serializeList
from bson import ObjectId


doctor = APIRouter()


@doctor.post("/doctor/", tags=["Doctor"])
async def insert_doctor(doctor: Doctor):
    conn.doctordb.doctor.insert_one(dict(doctor))
    return serializeList(conn.doctordb.doctor.find())


@doctor.get("/doctor/", tags=["Doctor"])
async def get_all_doctor():
    return serializeList(conn.doctordb.doctor.find())


@doctor.get("/doctor/{id}", tags=["Doctor"])
async def get_one_doctor(id):
    return serializeDict(conn.doctordb.doctor.find_one({"_id": ObjectId(id)}))


@doctor.put("/doctor/{id}", tags=["Doctor"])
async def update_doctor(id, doctor: Doctor):
    conn.doctordb.doctor.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(doctor)}
    )
    return serializeDict(conn.doctordb.doctor.find_one({"_id": ObjectId(id)}))


@doctor.delete("/doctor/{id}", tags=["Doctor"])
async def delete_doctor(id):
    return serializeDict(
        conn.doctordb.doctor.find_one_and_delete({"_id": ObjectId(id)})
    )
