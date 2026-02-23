#task_manager.py

from database import load_tasks, save_tasks

tasks = load_tasks()

def nomor_tugas():
    """Beri nomor untuk setiap tugas"""
    if not tasks:
        return 1
    return max(task["Nomor Tugas"] for task in tasks) + 1


def tambah_tugas(title, deadline, priority):
    """Menambahkan tugas baru"""
    tugas_baru = {
        "Nomor Tugas":nomor_tugas(),
        "Title": title,
        "Deadline": deadline,
        "Priority (easy, medium, hard)": priority,
        "Status": "Belum"
    }

    tasks.append(tugas_baru)
    save_tasks(tasks)
    return tugas_baru

def edit_task(nomor_task, new_data):
    """Edit berdasarkan nomor tugas"""
    for task in tasks:
        if task["Nomor Tugas"] == nomor_task:
            task.update(new_data)
            save_tasks(tasks)
            return True
        return False