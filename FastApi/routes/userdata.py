from fastapi import APIRouter, HTTPException
from models import Application
from database import userdata_collection  # Import the new collection

router = APIRouter()

@router.post("/submit-application/")
async def submit_application(application: Application):
    result = userdata_collection.insert_one(application.dict())
    if result.inserted_id:
        return {"message": "Application stored successfully"}
    else:
        raise HTTPException(status_code=500, detail="Error storing application")