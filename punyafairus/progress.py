def show_progress_bar(tasks):
    percentage = get_completion_percentage(tasks)
    bar_length = 30
    filled_length = int(bar_length * percentage // 100)

    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    print(f"Progress: |{bar}| {percentage:.2f}%")