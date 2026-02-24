#task_manager.py

import sys
import os

# Tambahkan folder punyadava ke path agar bisa import database
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "punyadava"))

from database import load_tasks, save_tasks


def _generate_id(tasks):
    """Beri nomor ID unik untuk setiap tugas baru."""
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def tambah_tugas(tasks, title):
    """Menambahkan tugas baru ke list dan simpan ke database."""
    tugas_baru = {
        "id": _generate_id(tasks),
        "title": title,
        "completed": False,
    }
    tasks.append(tugas_baru)
    save_tasks(tasks)
    return tasks


def edit_task(tasks, task_id, new_title):
    """Edit judul tugas berdasarkan ID."""
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = new_title
            break
    save_tasks(tasks)
    return tasks


def hapus_task(tasks, task_id):
    """Hapus tugas berdasarkan ID."""
    tasks = [t for t in tasks if t["id"] != task_id]
    save_tasks(tasks)
    return tasks


def mark_done(tasks, task_id):
    """Toggle status selesai/belum pada tugas."""
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            break
    save_tasks(tasks)
    return tasks


def get_all_tasks():
    """Mengembalikan semua tugas dari database."""
    return load_tasks()