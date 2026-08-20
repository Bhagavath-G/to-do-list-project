# 📝 Smart To-Do Application

A simple and beginner-friendly **To-Do List desktop application** built using **Python, Tkinter, and SQLite**.

This project allows users to add tasks, view saved tasks, and delete completed or unwanted tasks. The application uses SQLite for persistent local data storage, so tasks remain saved even after closing the application.

---

## 🚀 Features

* ➕ Add new tasks
* 📋 View all saved tasks
* 🗑️ Delete selected tasks
* 💾 Persistent task storage using SQLite
* 🖥️ Simple graphical user interface using Tkinter
* ⚡ Lightweight and fast
* 🔒 Uses parameterized SQL queries for database operations
* ❌ Input validation for empty tasks

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – GUI development
* **SQLite3** – Local database storage

No external Python packages are required.

---

## 📂 Project Structure

```text
Smart-To-Do-Application/
│
├── todo.py
├── todo_workspace.db
└── README.md
```

> `todo_workspace.db` will be automatically created when the application is run for the first time.

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Smart-To-Do-Application
```

### 3. Run the application

```bash
python todo.py
```

The Tkinter desktop application will open automatically.

---

## 🎯 How It Works

### 1. Add a Task

Enter a task in the input box and click:

**Add Task To Database**

The task is stored in the SQLite database.

### 2. View Tasks

All saved tasks are displayed in the application along with their unique Task ID.

### 3. Delete a Task

Select a task from the list and click:

**Delete Highlighted Task**

The selected task will be removed from the database and the list will refresh automatically.

---

## 🗄️ Database

The application uses an SQLite database named:

```text
todo_workspace.db
```

The database contains a `tasks` table:

| Column  | Type    | Description      |
| ------- | ------- | ---------------- |
| `id`    | INTEGER | Unique task ID   |
| `title` | TEXT    | Task description |

The `id` column uses `AUTOINCREMENT` to generate unique IDs automatically.

---

## 🔐 SQL Injection Protection

The application uses **parameterized SQL queries** when inserting and deleting tasks.

Example:

```python
cursor.execute(
    "INSERT INTO tasks (title) VALUES (?)",
    (task_text,)
)
```

This is safer than directly inserting user input into an SQL query.

---

## 📸 Application Preview

*Add a screenshot of your application here.*

Example:

```markdown
![Smart To-Do Application](screenshot.png)
```

---

## 🎓 Learning Outcomes

Through this project, I learned and practiced:

* Python functions
* Tkinter GUI development
* SQLite database connectivity
* CRUD operations
* SQL queries
* User input validation
* Exception handling
* Event-driven programming
* Connecting a GUI with a database
* Basic SQL injection prevention

---

## 🔮 Future Improvements

Possible improvements for future versions:

* ✏️ Edit existing tasks
* ✅ Mark tasks as completed
* 📅 Add due dates
* 🔍 Add task search
* 🏷️ Add task categories
* 🎨 Improve the user interface
* 🌙 Add dark mode
* 📊 Add task statistics
* 🔔 Add reminders

---

## 👨‍💻 Author

**Bhagavath Kumar G**

Computer Science Student | Python Learner | Aspiring Software Engineer

GitHub: **[@Bhagavath-G](https://github.com/Bhagavath-G)**

---

## ⭐ Support

If you found this project useful or you're also learning Python, feel free to **star ⭐ the repository** and explore the code.

---

### 📌 Project Status

**Completed ✅**

This project was created as a learning project to practice Python GUI development and database integration.
