#task_manager.py

from database import load_tasks, simpan_task

tasks = load_tasks()

def no_tugas():
    """Beri nomor untuk setiap tugas"""
    if not tasks:
        return 1
    return max(task["Nomor Tugas"] for task in tasks) + 1


def tambah_tugas(title, deadline, priority):
    """Menambahkan tugas baru"""
    tugas_baru = {
        "Nomor Tugas":no_tugas(),
        "Title": title,
        "Deadline": deadline,
        "Priority": priority,
        "Status": "Belum"
    }

    tasks.append(tugas_baru)
    simpan_task(tasks)
    return tugas_baru

def edit_task(nomor_task, new_data):
    """Edit berdasarkan Nomor Tugas"""
    for task in tasks:
        if task["Nomor Tugas"] == nomor_task:
            task.update(new_data)
            simpan_task(tasks)
            return True
    return False
    
def delete_task(nomor_task):
    """Hapus berdasarkan Nomor Tugas"""
    global tasks
    panjang = len(tasks)
    tasks = [task for task in tasks if task["Nomor Tugas"] != nomor_task]
    
    if len(tasks) < panjang:
        simpan_task(tasks)
        return True
    return False


def mark_done(nomor_task):
    """Tandai tugas selesai"""
    for task in tasks:
        if task["Nomor Tugas"] == nomor_task:
            task["Status"] = "Selesai"
            simpan_task(tasks)
            return True
    return False


def get_all_tasks():
    """Mengembalikan semua tugas"""
    return tasks