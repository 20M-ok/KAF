from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    due_date: Optional[datetime] = None

class Event(BaseModel):
    id: int
    title: str
    start: datetime
    end: datetime

class Reminder(BaseModel):
    id: int
    task_id: int
    remind_at: datetime

class UserPreference(BaseModel):
    id: int
    email: str
    notify_by_email: bool = True
