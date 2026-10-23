# DecodeLabs Python Programming Internship 🚀

This repository contains three projects completed during my **Python Programming Internship at DecodeLabs — 2026**. Each project includes **two versions**:

- **CLI (Command-Line Interface):** the original terminal-based Python program.
- **GUI (Web Interface):** a browser-based version built with Python and Django, with HTML and CSS and JavaScript where included.

The repository documents my progress in Python fundamentals and how the same core ideas can be presented through both a command-line program and a web interface.

---

## 🏆 Internship Certificate

[📄 View the DecodeLabs Internship Certificate (PDF)](./DecodeLabs%20Internship%20Certificate.pdf)

---

## 📂 Projects

### 📝 Project 1 — To-Do List

A task-management program available as a terminal menu and as a browser-based daily planner.

**CLI features**
- Add tasks and view them in a numbered list.
- Use a simple menu, handle invalid choices, and exit the program.

**Web UI features**
- Add tasks using a web form.
- View, search, complete, and delete tasks.
- See total, completed, and pending task counts.
- Save task records in the project's SQLite database.

**Concepts:** Python lists, `append()`, loops, conditional statements, `enumerate()`, user input, Django views and routes, HTML forms, and SQLite.

### 💰 Project 2 — Expense Tracker

An expense tracker available as a terminal program and as a browser-based spending dashboard.

**CLI features**
- Enter multiple expenses and see the running total.
- Review total, average, highest, and lowest expenses.
- View a numbered expense list; reject negative values and handle invalid input.

**Web UI features**
- Add expenses with an optional note.
- View recorded transactions and summary statistics.
- Calculate total spending, average, highest and lowest expense, and transaction count.
- Save expense records in the project's SQLite database.

**Concepts:** Python lists, loops, exception handling, numeric conversion and validation, accumulator pattern, `sum()`, `max()`, `min()`, Django, and SQLite.

### 🔐 Project 3 — Random Password Generator

A password generator available as a terminal program and as a browser-based tool.

**CLI features**
- Generate a password using a user-specified length.
- Require a length between 8 and 64 characters.
- Include uppercase letters, lowercase letters, digits, and symbols.
- Validate input and the generated password.

**Web UI features**
- Choose password length and character groups in the browser.
- Generate a password and show validation or input feedback.
- Use Python's `secrets` module for secure random selection.

**Concepts:** functions, string manipulation, `string`, `secrets`, lists, loops, conditional statements, exception handling, and input validation.

---

## 🛠️ Technologies Used

- **Python 3** — CLI programs and application logic
- **Django** — web framework for the GUI versions
- **HTML, CSS, JavaScript** — browser interface and client-side interactions where implemented
- **SQLite** — persistent data for the To-Do List and Expense Tracker web versions; a database file is also included with the Password Generator project
- **Git and GitHub** — version control and repository hosting

The command-line scripts use Python's standard library. The web UI versions require Django, listed in each app's `requirements.txt`.

---

## 📁 Repository Structure

```text
DecodeLabs-Internship-main/
├── README.md
├── DecodeLabs Internship Certificate.pdf
│
├── Project-1-To-Do-List/
│   ├── README.md
│   ├── to_do_list.py                 # CLI version
│   └── todo_list/                    # Web UI version
│       ├── app.py                    # Django settings, routes, and views
│       ├── index.html                # Web interface
│       ├── manage.py                 # Django command-line entry point
│       ├── requirements.txt
│       └── db.sqlite3                # SQLite database
│
├── Project-2-Expense-Tracker/
│   ├── README.md
│   ├── expense_tracker.py             # CLI version
│   └── expense_tracker/               # Web UI version
│       ├── app.py
│       ├── index.html
│       ├── manage.py
│       ├── requirements.txt
│       └── db.sqlite3
│
└── Project-3-Password-Generator/
    ├── README.md
    ├── password_generator.py          # CLI version
    └── password_generator/            # Web UI version
        ├── app.py
        ├── index.html
        ├── manage.py
        ├── requirements.txt
        └── db.sqlite3
```

Each web app keeps its Django configuration and routes in `app.py` to reduce the number of separate files. The included `db.sqlite3` files are retained; do not delete them if you need to preserve their existing data.

---

## ▶️ How to Run the Projects

### Requirements

- Python 3 installed
- Internet access may be needed the first time you install Django
- For the web versions, use the terminal in the relevant GUI folder shown below

### A. Run a CLI version

Open a terminal in the repository, then run the command for the project you want:

**Project 1 — To-Do List**

```bash
python Project-1-To-Do-List/to_do_list.py
```

**Project 2 — Expense Tracker**

```bash
python Project-2-Expense-Tracker/expense_tracker.py
```

**Project 3 — Random Password Generator**

```bash
python Project-3-Password-Generator/password_generator.py
```

On Windows, use `py` instead of `python` if that is how Python is configured on your system.

### B. Run a web UI version

Each web app is self-contained and has its own `requirements.txt`. Run the following steps **inside the relevant GUI folder**.

1. Open a terminal in one of these folders:
   - `Project-1-To-Do-List/todo_list/`
   - `Project-2-Expense-Tracker/expense_tracker/`
   - `Project-3-Password-Generator/password_generator/`
2. Create and activate a virtual environment (recommended):

   **Windows PowerShell**
   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependency and start Django:

   ```bash
   python -m pip install -r requirements.txt
   python manage.py runserver
   ```

4. Open **http://127.0.0.1:8000/** in your browser.
5. To stop the development server, press **Ctrl+C** in the terminal.

Run only one web app per port at a time. Stop the current server before starting another app on port `8000`, or configure a different port if you want to run multiple apps simultaneously.

> The Django development server is for local development, not production deployment. The SQLite database included with each web app is local to that project.

---

## 🎯 Learning Outcomes

Through these projects, I practised:

- Python programming fundamentals, lists, loops, and conditional logic
- Functions, string manipulation, and built-in modules
- Numeric calculations, accumulators, and input validation
- Exception handling and user-friendly error feedback
- Secure random generation with Python's `secrets` module
- Building web interfaces with Django, HTML, CSS, and JavaScript
- Handling form submissions and URL routes in Django
- Storing and retrieving data with SQLite
- Organizing code and documenting projects with README files
- Using Git and GitHub to manage and share project work

---

## 👩‍💻 Internship Information

- **Domain:** Python Programming
- **Organization:** DecodeLabs
- **Batch:** 2026

---

## 📌 About This Repository

This repository documents my project work and learning progress during the **DecodeLabs Python Programming Internship**. Each project includes its original CLI program, a web UI version, and project-specific documentation.

⭐ **Thank you for visiting this repository!**
