from typing import Dict, List, Optional
from .models import Task, Reminder

class InMemoryDB:
    """Simple in-memory storage for tasks and reminders."""

    def __init__(self) -> None:
        self.tasks: Dict[int, Task] = {}
        self.reminders: Dict[int, Reminder] = {}
        self.task_counter = 1
        self.reminder_counter = 1

    def create_task(self, task: Task) -> Task:
        task.id = self.task_counter
        self.tasks[self.task_counter] = task
        self.task_counter += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        return self.tasks.get(task_id)

    def update_task(self, task_id: int, task: Task) -> Optional[Task]:
        if task_id in self.tasks:
            task.id = task_id
            self.tasks[task_id] = task
            return task
        return None

    def delete_task(self, task_id: int) -> bool:
        return self.tasks.pop(task_id, None) is not None

    def list_tasks(self) -> List[Task]:
        return list(self.tasks.values())

    def create_reminder(self, reminder: Reminder) -> Reminder:
        reminder.id = self.reminder_counter
        self.reminders[self.reminder_counter] = reminder
        self.reminder_counter += 1
        return reminder

    def get_reminder(self, reminder_id: int) -> Optional[Reminder]:
        return self.reminders.get(reminder_id)

    def update_reminder(self, reminder_id: int, reminder: Reminder) -> Optional[Reminder]:
        if reminder_id in self.reminders:
            reminder.id = reminder_id
            self.reminders[reminder_id] = reminder
            return reminder
        return None

    def delete_reminder(self, reminder_id: int) -> bool:
        return self.reminders.pop(reminder_id, None) is not None

    def list_reminders(self) -> List[Reminder]:
        return list(self.reminders.values())


# Singleton instance
DB = InMemoryDB()
