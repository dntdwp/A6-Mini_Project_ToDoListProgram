#task_manager.py

from database import load_tasks, save_tasks

tasks = load_tasks()

def nomor_tugas():
    """Beri nomor untuk setiap tugas"""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1

