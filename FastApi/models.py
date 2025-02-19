from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Job(BaseModel):
    title: str
    company: str
    location: str
    job_detail: str  # Added job_detail field
    duration: Optional[str] = None
    stipend: Optional[str] = None
    posted_on: str
    offer: Optional[str] = None
    date: datetime

class Application(BaseModel):
    fullName: str
    email: str
    phone: str
    location: str
    linkedIn: str = None
    github: str = None
    profileSummary: str
    skills: str
    education: str
    workExperience: str
    certifications: str = None
    projects: str = None
    languages: str
    coverLetterNotes: str