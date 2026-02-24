from datetime import datetime

def filter_by_status(tasks, status):
    filtered = []
    for task in tasks:
        task_status = task.get('status', '').lower()
        if task_status == status.lower():
            filtered.append(task)
    return filtered

def filter_by_priority(tasks, priority):
    filtered = []
    for task in tasks:
        task_priority = task.get('prioritas', '').lower()
        if task_priority == priority.lower():
            filtered.append(task)
    return filtered

def sort_by_deadline(tasks):
    def get_date(task):
        try:
            return datetime.strptime(task['deadline'], "%Y-%m-%d")
        except ValueError:
            return datetime.max
    return sorted(tasks, key=get_date)

def search_task(tasks, keyword):
    results = []
    keyword = keyword.lower()
    
    for task in tasks:
        title = task.get('judul', '').lower()
        if keyword in title:
            results.append(task)
    return results
