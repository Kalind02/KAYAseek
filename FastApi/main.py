from fastapi import FastAPI, Query
from pymongo import MongoClient
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

# Initialize FastAPI
app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.Jobsdata
collection = db["internships"]

# Job Data Model
class Job(BaseModel):
    title: str
    company: str
    location: str
    duration: Optional[str] = None
    stipend: Optional[str] = None
    posted_on: str
    offer: Optional[str] = None
    date: datetime

# Fetch all jobs with optional filters
@app.get("/jobs", response_model=List[Job])
def get_jobs(
    company: Optional[str] = Query(None),
    location: Optional[str] = Query(None),
    duration: Optional[str] = Query(None),
    stipend: Optional[str] = Query(None),
    limit: Optional[int] = Query(None),  # Allow user to specify limit or return all
    page: int = Query(1, ge=1)
):
    query = {}

    if company:
        query["company"] = {"$regex": f"^{company}$", "$options": "i"}

    if location:
        query["location"] = {"$regex": f"\\b{location}\\b", "$options": "i"}

    if duration:
        query["duration"] = {"$regex": f"^{duration}$", "$options": "i"}

    if stipend:
        query["stipend"] = {"$regex": f"^{stipend}$", "$options": "i"}

    cursor = collection.find(query, {"_id": 0})  # Apply filters correctly

    if limit:
        cursor = cursor.limit(limit).skip((page - 1) * limit)  # Apply pagination only if limit is set

    jobs = list(cursor)
    return jobs if jobs else []

