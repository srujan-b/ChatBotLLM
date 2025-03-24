from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static frontend files
app.mount("/static", StaticFiles(directory="client"), name="static")

# Serve the index.html at root
@app.get("/")
async def serve_home():
    return FileResponse(os.path.join("client", "index.html"))

# Include your existing API routers below
from app.api.v1 import endpoints

app.include_router(endpoints.router)

# Optional startup/shutdown events
@app.on_event("startup")
async def startup_event():
    print("API starting up!")

@app.on_event("shutdown")
async def shutdown_event():
    print("API shutting down!")
