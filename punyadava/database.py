import json
import os
import shutil
from datetime import datetime

# Konfigurasi nama file — gunakan path absolut relatif terhadap project root
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_FILE = os.path.join(_PROJECT_ROOT, "tasks.json")
BACKUP_FILE = os.path.join(_PROJECT_ROOT, "tasks_backup.json")

def load_tasks():
    """Membaca semua data tugas dari file JSON."""
    if not os.path.exists(DB_FILE):
        return []  # Kembalikan list kosong jika file belum ada
    
    try:
        with open(DB_FILE, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    """Menyimpan list tugas ke file JSON dengan backup otomatis."""
    try:
        # 1. Backup file lama sebelum menimpa dengan yang baru
        if os.path.exists(DB_FILE):
            shutil.copy(DB_FILE, BACKUP_FILE)
            
        # 2. Simpan data baru
        with open(DB_FILE, "w") as file:
            json.dump(tasks, file, indent=4)
        return True
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")
        return False

def update_task_in_db(task_id, updated_data):
    """Mencari tugas berdasarkan ID dan memperbarui datanya."""
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task.get("id") == task_id:
            tasks[i].update(updated_data)
            break
    return save_tasks(tasks)

def delete_task_from_db(task_id):
    """Menghapus tugas dari database berdasarkan ID."""
    tasks = load_tasks()
    # Filter list: ambil semua kecuali yang ID-nya cocok
    new_tasks = [t for t in tasks if t.get("id") != task_id]
    
    if len(new_tasks) < len(tasks):
        return save_tasks(new_tasks)
    return False

def auto_backup():
    """Fungsi tambahan untuk membuat backup manual dengan timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_tasks_{timestamp}.json"
    if os.path.exists(DB_FILE):
        shutil.copy(DB_FILE, backup_name)
        return backup_name
    return None