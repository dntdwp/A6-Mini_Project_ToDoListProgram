import importlib.util
import os
import taskmanager


def load_tasks():
    return taskmanager.get_all_tasks()


def add_task(title, deadline, priority):
    return taskmanager.tambah_tugas(title, deadline, priority)


def edit_task(nomor_task, new_data):
    return taskmanager.edit_task(nomor_task, new_data)


def delete_task(nomor_task):
    return taskmanager.hapus_task(nomor_task)


def mark_done(nomor_task):
    return taskmanager.mark_done(nomor_task)


if __name__ == "__main__":
    ui_path = os.path.join(os.path.dirname(__file__), "punya danang", "ui.py")

    spec = importlib.util.spec_from_file_location("ui", ui_path)
    ui = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ui)

    ui.run()
