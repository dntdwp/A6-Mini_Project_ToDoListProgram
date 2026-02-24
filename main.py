import importlib.util
import os
import sys

# Tambahkan folder modul ke sys.path agar bisa di-import
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "punyafathimah"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "punyadava"))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "punyafairus"))

import taskmanager
import report


def load_tasks():
    return taskmanager.get_all_tasks()


def add_task(tasks, title):
    return taskmanager.tambah_tugas(tasks, title)


def toggle_task(tasks, task_id):
    return taskmanager.mark_done(tasks, task_id)


def edit_task(tasks, task_id, new_title):
    return taskmanager.edit_task(tasks, task_id, new_title)


def delete_task(tasks, task_id):
    return taskmanager.hapus_task(tasks, task_id)


# ── Report & progress functions ─────────────────────────────────
def get_report_text(tasks):
    return report.build_report_text(tasks)


def export_report(tasks):
    return report.export_report(tasks)


def get_progress(tasks):
    return report.get_completion_percentage(tasks)


def get_progress_bar(tasks):
    return report.get_progress_bar(tasks)


if __name__ == "__main__":
    ui_path = os.path.join(os.path.dirname(__file__), "punya danang", "ui.py")

    spec = importlib.util.spec_from_file_location("ui", ui_path)
    ui = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ui)

    ui.run()
