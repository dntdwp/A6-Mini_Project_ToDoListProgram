import importlib.util
import os
import json

# ── Data file path ──────────────────────────────────────────────
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def _save_tasks(tasks):
    """Persist tasks list to JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def load_tasks():
    """Load tasks from JSON file. Returns an empty list if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _next_id(tasks):
    """Return the next available task ID."""
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def add_task(tasks, title):
    """Add a new task and return the updated list."""
    task = {"id": _next_id(tasks), "title": title.strip(), "completed": False}
    tasks.append(task)
    _save_tasks(tasks)
    return tasks


def toggle_task(tasks, task_id):
    """Toggle the completed status of a task and return the updated list."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    _save_tasks(tasks)
    return tasks


def delete_task(tasks, task_id):
    """Delete a task by ID and return the updated list."""
    tasks = [t for t in tasks if t["id"] != task_id]
    _save_tasks(tasks)
    return tasks


def edit_task(tasks, task_id, new_title):
    """Edit a task's title and return the updated list."""
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title.strip()
            break
    _save_tasks(tasks)
    return tasks


# ── Import & launch UI ─────────────────────────────────────────
# Import ui.py from "punya danang" folder (space in name requires importlib)
ui_path = os.path.join(os.path.dirname(__file__), "punya danang", "ui.py")
spec = importlib.util.spec_from_file_location("ui", ui_path)
ui = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ui)
