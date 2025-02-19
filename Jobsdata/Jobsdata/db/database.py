from pymongo import MongoClient
from datetime import datetime, timezone, timedelta

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.KAYAseek
internships_collection = db["internships"]

# Insert into database
def insert_to_db(title, job_detail, company, location, duration, stipend, posted_on, offer):
    job_id = f"{title}-{company}".lower().replace(" ", "-")

    data = {
        "_id": job_id,
        "job_detail": job_detail,
        "title": title,
        "company": company,
        "location": location,
        "duration": duration,
        "stipend": stipend,
        "posted_on": posted_on,
        "offer": offer,
        "date": datetime.now(timezone.utc)
    }
    
    result = internships_collection.update_one({"_id": job_id}, {"$set": data}, upsert=True)
    return result.matched_count == 0  # Returns True if a new job was inserted

# Delete old jobs after X days
def delete_old_jobs(days=30):
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
    result = internships_collection.delete_many({"date": {"$lt": cutoff_date}})
    print(f"Deleted {result.deleted_count} old job listings.")
