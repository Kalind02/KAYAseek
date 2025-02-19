from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.jobs import router as job_router
from routes.userdata import router as userdata_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or ["*"] for all origins (use with caution)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the Jobs router
app.include_router(job_router)

# Include the Userdata router
app.include_router(userdata_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Runs the app on port 8000
