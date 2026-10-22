# Expense Tracker — Personal Finance Dashboard

A browser-based expense tracking application built with Python and Django, using HTML, CSS, and JavaScript for the interface. It converts a console-based expense calculator into a visual dashboard for recording expenses and reviewing spending summaries.

## Features

- Record an expense amount and an optional note.
- Display recorded transactions in a list or ledger.
- Calculate total spending.
- Calculate average, highest, and lowest expense values.
- Display the number of recorded transactions.
- Provide a clear financial overview at a glance.
- Validate expense input, including invalid or negative amounts where enforced by the application.
- Use a responsive interface for different screen sizes.

The available features depend on the current implementation. If a feature is not present in the UI, remove it from this list before publishing.

## Technology Stack

- **Python 3** — application logic and calculations
- **Django** — web framework, views, templates, and data handling
- **HTML** — forms, dashboard structure, and transaction presentation
- **CSS** — finance dashboard styling and responsive layout
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
expense_tracker/
├── manage.py
├── requirements.txt
├── config/
├── expenses/
├── templates/
├── static/
└── README.md
```

- `manage.py` — Django command-line utility used to run the application.
- `config/` — project settings and URL configuration.
- `expenses/` — expense-related application logic and data models.
- `templates/` — Django HTML templates.
- `static/` — CSS, JavaScript, and other static assets.
- `requirements.txt` — Python dependencies.

## Concepts Practised

- Python lists, functions, and conditional logic
- Numeric conversion and expense calculations
- Input validation and exception handling
- Django views, URL routing, templates, and models
- HTML forms and displaying transaction data
- CSS dashboard layout and responsive design
- JavaScript interactions
- Database migrations and CRUD-style workflows

## Learning Outcome

This project demonstrates how Python calculation logic can power a web-based finance dashboard. It combines data entry, validation, summary calculations, Django's request/response flow, and frontend presentation.

## Notes

Run this project independently from the other applications. Each application has its own Django configuration and should be started from its own project directory.
