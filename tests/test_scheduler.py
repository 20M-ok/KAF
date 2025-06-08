from datetime import datetime, timedelta
from fastapi.testclient import TestClient
from backend.scheduler.main import app

client = TestClient(app)

def test_create_and_get_task():
    resp = client.post('/tasks', json={'id': 0, 'title': 'Sample'})
    assert resp.status_code == 200
    task = resp.json()
    task_id = task['id']

    resp = client.get(f'/tasks/{task_id}')
    assert resp.status_code == 200
    assert resp.json()['title'] == 'Sample'

def test_create_reminder_for_task():
    task_resp = client.post('/tasks', json={'id': 0, 'title': 'Task with Reminder'})
    task_id = task_resp.json()['id']

    remind_at = (datetime.utcnow() + timedelta(days=1)).isoformat()
    rem_resp = client.post('/reminders', json={'id': 0, 'task_id': task_id, 'remind_at': remind_at})
    assert rem_resp.status_code == 200
    reminder = rem_resp.json()
    assert reminder['task_id'] == task_id

    get_resp = client.get(f"/reminders/{reminder['id']}")
    assert get_resp.status_code == 200
