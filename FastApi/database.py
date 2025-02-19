from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.Jobsdata
internship_collection = db["internships"]
userdata_collection = db["userdata"]