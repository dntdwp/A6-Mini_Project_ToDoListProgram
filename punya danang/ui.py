import tkinter as tk
from tkinter import messagebox, simpledialog
import sys
import os

# Add project root to path so we can import main
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import main as todo


# ── Colour palette ──────────────────────────────────────────────
BG          = "#1e1e2e"
SIDEBAR     = "#181825"
ACCENT      = "#89b4fa"
ACCENT_HOVER = "#74c7ec"
TEXT        = "#cdd6f4"
SUBTEXT     = "#a6adc8"
SURFACE     = "#313244"
GREEN       = "#a6e3a1"
RED         = "#f38ba8"
YELLOW      = "#f9e2af"


class TodoApp(tk.Tk):
    """Simple To-Do List GUI using Tkinter."""

    def __init__(self):
        super().__init__()
        self.title("📝  To-Do List")
        self.geometry("520x600")
        self.configure(bg=BG)
        self.resizable(False, False)

        self.tasks = todo.load_tasks()

        self._build_header()
        self._build_input_area()
        self._build_task_list()
        self._build_footer()
        self._refresh_list()

    # ── Header ──────────────────────────────────────────────────
    def _build_header(self):
        header = tk.Frame(self, bg=SIDEBAR, pady=14)
        header.pack(fill=tk.X)

        tk.Label(
            header, text="📝  To-Do List", font=("Segoe UI", 18, "bold"),
            bg=SIDEBAR, fg=ACCENT,
        ).pack()

        tk.Label(
            header, text="Kelompok A6 – Mini Project", font=("Segoe UI", 9),
            bg=SIDEBAR, fg=SUBTEXT,
        ).pack()

    # ── Input area ──────────────────────────────────────────────
    def _build_input_area(self):
        frame = tk.Frame(self, bg=BG, pady=10, padx=20)
        frame.pack(fill=tk.X)

        self.entry = tk.Entry(
            frame, font=("Segoe UI", 12), bg=SURFACE, fg=TEXT,
            insertbackground=TEXT, relief=tk.FLAT, bd=8,
        )
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.entry.bind("<Return>", lambda e: self._add_task())

        add_btn = tk.Button(
            frame, text="＋ Add", font=("Segoe UI", 11, "bold"),
            bg=ACCENT, fg="#11111b", activebackground=ACCENT_HOVER,
            relief=tk.FLAT, padx=14, pady=6, cursor="hand2",
            command=self._add_task,
        )
        add_btn.pack(side=tk.RIGHT, padx=(8, 0))

    # ── Scrollable task list ────────────────────────────────────
    def _build_task_list(self):
        container = tk.Frame(self, bg=BG, padx=20)
        container.pack(fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(container, bg=BG, highlightthickness=0)
        scrollbar = tk.Scrollbar(container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollable = tk.Frame(self.canvas, bg=BG)

        self.scrollable.bind(
            "<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        self.canvas.create_window((0, 0), window=self.scrollable, anchor=tk.NW)
        self.canvas.configure(yscrollcommand=scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Mouse-wheel scrolling
        self.canvas.bind_all(
            "<MouseWheel>", lambda e: self.canvas.yview_scroll(-int(e.delta / 120), "units")
        )

    # ── Footer with stats ───────────────────────────────────────
    def _build_footer(self):
        self.footer = tk.Label(
            self, font=("Segoe UI", 9), bg=SIDEBAR, fg=SUBTEXT, pady=6,
        )
        self.footer.pack(fill=tk.X, side=tk.BOTTOM)

    # ── Actions ─────────────────────────────────────────────────
    def _add_task(self):
        title = self.entry.get()
        if not title.strip():
            return
        self.tasks = todo.add_task(self.tasks, title)
        self.entry.delete(0, tk.END)
        self._refresh_list()

    def _toggle_task(self, task_id):
        self.tasks = todo.toggle_task(self.tasks, task_id)
        self._refresh_list()

    def _delete_task(self, task_id):
        if messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?"):
            self.tasks = todo.delete_task(self.tasks, task_id)
            self._refresh_list()

    def _edit_task(self, task_id, current_title):
        new_title = simpledialog.askstring(
            "Edit Task", "New title:", initialvalue=current_title, parent=self,
        )
        if new_title is not None:
            self.tasks = todo.edit_task(self.tasks, task_id, new_title)
            self._refresh_list()

    # ── Refresh the displayed list ──────────────────────────────
    def _refresh_list(self):
        # Clear existing widgets
        for w in self.scrollable.winfo_children():
            w.destroy()

        if not self.tasks:
            tk.Label(
                self.scrollable, text="No tasks yet — add one above!",
                font=("Segoe UI", 11), bg=BG, fg=SUBTEXT, pady=30,
            ).pack()
        else:
            for task in self.tasks:
                self._create_task_row(task)

        # Update footer stats
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t["completed"])
        self.footer.config(text=f"  {done} / {total} tasks completed")

    def _create_task_row(self, task):
        row = tk.Frame(self.scrollable, bg=SURFACE, pady=6, padx=10)
        row.pack(fill=tk.X, pady=3)

        # Checkbox
        check_text = "✔" if task["completed"] else "○"
        check_color = GREEN if task["completed"] else SUBTEXT
        chk = tk.Label(
            row, text=check_text, font=("Segoe UI", 14),
            bg=SURFACE, fg=check_color, cursor="hand2",
        )
        chk.pack(side=tk.LEFT, padx=(0, 8))
        chk.bind("<Button-1>", lambda e, tid=task["id"]: self._toggle_task(tid))

        # Title
        title_font = ("Segoe UI", 11)
        title_fg = SUBTEXT if task["completed"] else TEXT
        overstrike = task["completed"]
        lbl = tk.Label(
            row, text=task["title"], font=title_font,
            bg=SURFACE, fg=title_fg, anchor=tk.W,
        )
        if overstrike:
            lbl.configure(font=("Segoe UI", 11, "overstrike"))
        lbl.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Edit button
        edit_btn = tk.Label(
            row, text="✏", font=("Segoe UI", 12), bg=SURFACE, fg=YELLOW, cursor="hand2",
        )
        edit_btn.pack(side=tk.RIGHT, padx=4)
        edit_btn.bind(
            "<Button-1>",
            lambda e, tid=task["id"], t=task["title"]: self._edit_task(tid, t),
        )

        # Delete button
        del_btn = tk.Label(
            row, text="✖", font=("Segoe UI", 12), bg=SURFACE, fg=RED, cursor="hand2",
        )
        del_btn.pack(side=tk.RIGHT, padx=4)
        del_btn.bind("<Button-1>", lambda e, tid=task["id"]: self._delete_task(tid))


def run():
    app = TodoApp()
    app.mainloop()


if __name__ == "__main__":
    run()
