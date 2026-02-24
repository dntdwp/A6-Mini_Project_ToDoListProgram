from datetime import datetime
import os


# ── Progress helpers ────────────────────────────────────────────
def get_completion_percentage(tasks):
    """Return the completion percentage of tasks."""
    if not tasks:
        return 0.0
    completed = sum(1 for t in tasks if t.get("completed", False))
    return (completed / len(tasks)) * 100


def get_progress_bar(tasks):
    """Return a text-based progress bar string."""
    percentage = get_completion_percentage(tasks)
    bar_length = 30
    filled = int(bar_length * percentage // 100)
    bar = "█" * filled + "─" * (bar_length - filled)
    return f"|{bar}| {percentage:.1f}%"


# ── Report helpers ──────────────────────────────────────────────

# 1️⃣ Jumlah tugas selesai vs belum
def get_summary(tasks):
    completed = 0
    not_completed = 0

    for task in tasks:
        if task.get("completed", False):
            completed += 1
        else:
            not_completed += 1

    return completed, not_completed


# 2️⃣ Tugas yang sudah melewati deadline (hanya jika task punya field deadline)
def get_overdue_tasks(tasks):
    overdue_tasks = []
    today = datetime.today().date()

    for task in tasks:
        deadline_str = task.get("deadline")
        if not deadline_str:
            continue  # skip tasks tanpa deadline
        try:
            deadline_date = datetime.strptime(deadline_str, "%Y-%m-%d").date()
        except (ValueError, TypeError):
            continue
        if not task.get("completed", False) and deadline_date < today:
            overdue_tasks.append(task)

    return overdue_tasks


# 3️⃣ Build report text (reusable for display and export)
def build_report_text(tasks):
    completed, not_completed = get_summary(tasks)
    overdue = get_overdue_tasks(tasks)
    percentage = get_completion_percentage(tasks)
    progress = get_progress_bar(tasks)

    lines = [
        "═══════ LAPORAN TO-DO LIST ═══════",
        "",
        f"  Total tugas            : {completed + not_completed}",
        f"  Tugas selesai          : {completed}",
        f"  Tugas belum selesai    : {not_completed}",
        f"  Progress               : {progress}",
        "",
    ]

    if overdue:
        lines.append("  Tugas melewati deadline:")
        for task in overdue:
            lines.append(f"    • {task['title']}  (Deadline: {task.get('deadline', '-')})")
    else:
        lines.append("  Tidak ada tugas yang terlambat. ✔")

    lines += ["", "══════════════════════════════════"]
    return "\n".join(lines)


# 4️⃣ Export laporan ke file .txt
def export_report(tasks, filename="report_todolist.txt"):
    _PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(_PROJECT_ROOT, filename)

    report = build_report_text(tasks)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report + "\n")
    return filepath