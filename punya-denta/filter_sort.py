from datetime import datetime

def filter_by_status(tasks, status):
    target_status = status.lower()
    return [task for task in tasks if (task.get('status') or '').lower() == target_status]

def filter_by_priority(tasks, priority):
    target_priority = priority.lower()
    return [task for task in tasks if (task.get('prioritas') or '').lower() == target_priority]

def sort_by_deadline(tasks):
    return sorted(tasks, key=lambda task: task.get('deadline') or '9999-99-99')

def search_task(tasks, keyword):
    target_keyword = keyword.lower()
    return [task for task in tasks if target_keyword in (task.get('judul') or '').lower()]
