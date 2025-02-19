from fastapi import APIRouter, Query
from database import internship_collection
from models import Job
from typing import List, Optional

router = APIRouter(prefix="/jobs", tags=["Jobs"])

@router.get("/", response_model=List[Job])
def get_jobs(
    company: Optional[str] = Query(None, description="Filter by company name"),
    location: Optional[str] = Query(None, description="Filter by location"),
    limit: int = Query(10, ge=1, description="Number of jobs per page"),
    page: int = Query(1, ge=1, description="Page number")
):
    query = {}

    if company:
        query["company"] = {"$regex": f"^{company}$", "$options": "i"}

    if location:
        query["location"] = {"$regex": f"\\b{location}\\b", "$options": "i"}
    
    cursor = internship_collection.find(query, {"_id": 0})
    # Apply pagination: skip and limit
    cursor = cursor.skip((page - 1) * limit).limit(limit)
    jobs = list(cursor)
    return jobs
