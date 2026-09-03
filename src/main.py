from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from data.mock_data import mock_milestones_data
from services.tracking_service import (
    get_milestones,
    update_milestone_status,
    update_task_status,
)

app = FastAPI(
    title="BuildTrack API",
    description="API for managing construction projects, milestones, and tracking progress.",
    version="0.1.0"
)


class MilestoneStatusUpdate(BaseModel):
    status: str


class TaskStatusUpdate(BaseModel):
    status: str

@app.get("/")
def read_root():
    return get_milestones()

@app.get("/milestones")
def read_milestones():
    return get_milestones()


@app.patch("/milestones/{milestone_id}/status")
def update_milestone(milestone_id: str, update: MilestoneStatusUpdate):
    try:
        return update_milestone_status(milestone_id, update.status)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
    except ValueError as error:
        raise HTTPException(status_code=400, detail=str(error)) from error


@app.patch("/tasks/{task_id}/status")
def update_task(task_id: str, update: TaskStatusUpdate):
    try:
        return update_task_status(task_id, update.status)
    except LookupError as error:
        raise HTTPException(status_code=404, detail=str(error)) from error
