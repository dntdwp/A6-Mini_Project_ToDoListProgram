def get_completion_percentage(tasks):
    """Return the completion percentage of tasks."""
    if not tasks:
        return 0.0
    completed = sum(1 for t in tasks if t.get("completed", False))
    return (completed / len(tasks)) * 100


def show_progress_bar(tasks):
    percentage = get_completion_percentage(tasks)
    bar_length = 30
    filled_length = int(bar_length * percentage // 100)

    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    print(f"Progress: |{bar}| {percentage:.2f}%")