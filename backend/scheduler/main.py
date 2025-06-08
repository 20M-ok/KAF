from fastapi import FastAPI, HTTPException
from .models import Task, Reminder
from .database import DB

app = FastAPI(title="Scheduler API")

@app.post("/tasks", response_model=Task)
def create_task(task: Task) -> Task:
    return DB.create_task(task)

@app.get("/tasks", response_model=list[Task])
def list_tasks():
    return DB.list_tasks()

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int) -> Task:
    task = DB.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task) -> Task:
    updated = DB.update_task(task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if not DB.delete_task(task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"ok": True}

@app.post("/reminders", response_model=Reminder)
def create_reminder(reminder: Reminder) -> Reminder:
    if not DB.get_task(reminder.task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    return DB.create_reminder(reminder)

@app.get("/reminders", response_model=list[Reminder])
def list_reminders():
    return DB.list_reminders()

@app.get("/reminders/{reminder_id}", response_model=Reminder)
def get_reminder(reminder_id: int) -> Reminder:
    reminder = DB.get_reminder(reminder_id)
    if not reminder:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return reminder

@app.put("/reminders/{reminder_id}", response_model=Reminder)
def update_reminder(reminder_id: int, reminder: Reminder) -> Reminder:
    if not DB.get_task(reminder.task_id):
        raise HTTPException(status_code=404, detail="Task not found")
    updated = DB.update_reminder(reminder_id, reminder)
    if not updated:
        raise HTTPException(status_code=404, detail="Reminder not found")
    return updated

@app.delete("/reminders/{reminder_id}")
def delete_reminder(reminder_id: int):
    if not DB.delete_reminder(reminder_id):
        raise HTTPException(status_code=404, detail="Reminder not found")
    return {"ok": True}
