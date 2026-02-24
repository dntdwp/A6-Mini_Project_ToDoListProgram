from report import *

tasks = [
    {"title": "Kerjakan laporan", "deadline": "2026-02-20", "completed": True},
    {"title": "Belajar Python", "deadline": "2026-02-10", "completed": False},
    {"title": "Meeting", "deadline": "2026-02-15", "completed": False},
]

print("Ringkasan:")
completed, not_completed = get_summary(tasks)
print("Selesai:", completed)
print("Belum selesai:", not_completed)

print("\nTugas Terlambat:")
overdue = get_overdue_tasks(tasks)
for task in overdue:
    print("-", task["title"])

show_progress_bar(tasks)

export_report(tasks, "laporan.txt")
print("\nLaporan berhasil disimpan ke laporan.txt")