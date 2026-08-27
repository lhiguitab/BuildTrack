from fastapi import FastAPI
from data.mock_data import mock_milestones_data
from services.tracking_service import get_milestones

app = FastAPI(
    title="BuildTrack API",
    description="API for managing construction projects, milestones, and tracking progress.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return get_milestones()

@app.get("/milestones")
def read_milestones():
    return get_milestones()