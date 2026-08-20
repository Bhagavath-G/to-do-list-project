import sqlite3
import tkinter as tk
from tkinter import messagebox


# ============================================================
# STEP 1: INITIALIZE DATABASE
# ============================================================

def init_db():
    # Connect to database (creates the file if it doesn't exist)
    conn = sqlite3.connect("todo_workspace.db")
    cursor = conn.cursor()

    # Create tasks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# ============================================================
# STEP 2: ADD TASK
# ============================================================

def add_task():
    # Get text from entry box
    task_text = task_entry.get().strip()

    # Check if the input is empty
    if task_text == "":
        messagebox.showwarning(
            "Validation Error",
            "Task entry description cannot be empty!"
        )
        return

    # Connect to database
    conn = sqlite3.connect("todo_workspace.db")
    cursor = conn.cursor()

    # Insert task into database
    cursor.execute(
        "INSERT INTO tasks (title) VALUES (?)",
        (task_text,)
    )

    conn.commit()
    conn.close()

    # Clear input box
    task_entry.delete(0, tk.END)

    # Refresh task list
    load_tasks()

    messagebox.showinfo(
        "Success",
        "New task added successfully!"
    )


# ============================================================
# STEP 3: LOAD TASKS
# ============================================================

def load_tasks():
    # Clear existing list
    task_listbox.delete(0, tk.END)

    # Connect to database
    conn = sqlite3.connect("todo_workspace.db")
    cursor = conn.cursor()

    # Get all tasks
    cursor.execute(
        "SELECT id, title FROM tasks ORDER BY id DESC"
    )

    rows = cursor.fetchall()

    conn.close()

    # Display tasks in Listbox
    for row in rows:
        task_listbox.insert(
            tk.END,
            f"{row[1]} (Task ID: {row[0]})"
        )


# ============================================================
# STEP 4: DELETE TASK
# ============================================================

def delete_task():
    try:
        # Get selected task
        selected_text = task_listbox.get(
            task_listbox.curselection()
        )

        # Extract task ID
        task_id = selected_text.split(
            "(Task ID: "
        )[1].replace(")", "")

        # Connect to database
        conn = sqlite3.connect("todo_workspace.db")
        cursor = conn.cursor()

        # Delete selected task
        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()
        conn.close()

        # Refresh list
        load_tasks()

        messagebox.showinfo(
            "Removed",
            "Task deleted successfully!"
        )

    except tk.TclError:
        messagebox.showwarning(
            "Selection Error",
            "Please highlight a specific task to remove."
        )


# ============================================================
# STEP 5: INITIALIZE DATABASE
# ============================================================

init_db()


# ============================================================
# STEP 6: CREATE MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title("Smart To-Do Application")
root.geometry("360x420")
root.resizable(False, False)


# ============================================================
# STEP 7: CREATE GUI COMPONENTS
# ============================================================

# Task label
tk.Label(
    root,
    text="Enter New Task Description:",
    font=("Arial", 10, "bold")
).pack(pady=(15, 2))


# Task input box
task_entry = tk.Entry(
    root,
    width=36
)
task_entry.pack(pady=2)


# Add task button
add_button = tk.Button(
    root,
    text="Add Task To Database",
    bg="#c6f6d5",
    fg="#22543d",
    font=("Arial", 9, "bold"),
    command=add_task
)
add_button.pack(pady=10)


# Separator
tk.Frame(
    root,
    height=2,
    bd=1,
    relief="sunken"
).pack(
    fill="x",
    padx=20,
    pady=5
)


# Active tasks label
tk.Label(
    root,
    text="Active Logged Storage Entries:",
    font=("Arial", 10, "bold")
).pack(pady=5)


# Task list
task_listbox = tk.Listbox(
    root,
    width=40,
    height=10
)
task_listbox.pack(pady=5)


# Delete button
delete_button = tk.Button(
    root,
    text="Delete Highlighted Task",
    bg="#fed7d7",
    fg="#742a2a",
    font=("Arial", 9),
    command=delete_task
)
delete_button.pack(pady=10)


# ============================================================
# STEP 8: LOAD EXISTING TASKS
# ============================================================

load_tasks()


# ============================================================
# STEP 9: START APPLICATION
# ============================================================

root.mainloop()