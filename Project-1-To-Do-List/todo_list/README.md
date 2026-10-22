# To-Do List — Daily Planner

A browser-based task management application built with Django and Python, with an HTML, CSS, and JavaScript interface. It turns the original console-based task list into a visual planner for adding, reviewing, searching, and tracking tasks.

## Features

- Add tasks through a web form.
- View tasks in a structured task list.
- Mark tasks as completed and review remaining work.
- View task summaries, including total, completed, and pending tasks.
- Search tasks.
- Receive clear feedback for form actions and invalid input.
- Use a responsive layout on desktop and smaller screens.

> Available actions depend on the current implementation in the project. Keep this list aligned with the controls and views included in your version.

## Technology Stack

- **Python 3** — application logic
- **Django** — web framework, routing, views, templates, and data handling
- **HTML** — page structure
- **CSS** — layout, responsive styling, and visual design
- **JavaScript** — client-side interactions where implemented
- **SQLite** — default development database, if configured in the project

## How to Run

### Requirements

- Python 3 installed
- A terminal opened in this project folder

### Setup

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Apply database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open **http://127.0.0.1:8000/** in your browser.

To stop the server, press `Ctrl+C` in the terminal.

## Project Structure

The exact folders may vary slightly by version.

```text
todo_list/
├── manage.py
├── requirements.txt
├── config/
├── tasks/
├── templates/
├── static/
└── README.md
```

- `manage.py` — Django command-line utility used to run the application.
- `config/` — project settings and URL configuration.
- `tasks/` — task-related application logic and data models.
- `templates/` — Django HTML templates.
- `static/` — CSS, JavaScript, and other static assets.
- `requirements.txt` — Python dependencies.

## Concepts Practised

- Python functions, lists, and conditional logic
- Django views, URL routing, templates, and models
- HTML forms and template rendering
- CSS layout and responsive design
- JavaScript interactions
- Input validation and task-state handling
- Database migrations and CRUD-style workflows

## Learning Outcome

This project demonstrates how a simple task-management program can be developed into a browser-based application. It combines Python fundamentals with Django's request/response flow and frontend technologies to create a more accessible user interface.

## Notes

Run this project independently from the other applications. Each application has its own Django configuration and should be started from its own project directory.
