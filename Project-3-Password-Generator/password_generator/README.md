# Password Generator — Security Studio

A browser-based password generation tool built with Python and Django, with an HTML, CSS, and JavaScript interface. The UI lets users configure password options and generate a password without using a console prompt.

## Features

- Choose a password length within the supported range.
- Select character groups such as uppercase letters, lowercase letters, numbers, and symbols.
- Generate a password based on the selected options.
- Display the generated password in the interface.
- Provide an action to copy the generated password if implemented in the current version.
- Validate configuration and provide feedback when the options cannot produce a valid password.
- Present password-generation controls in a responsive interface.

For security, verify that the current implementation uses Python's `secrets` module for generating password characters. Do not describe a password generator as cryptographically secure unless the implementation supports that claim.

## Technology Stack

- **Python 3** — password-generation logic
- **Django** — web framework, views, routing, and template rendering
- **HTML** — form controls and result presentation
- **CSS** — interface layout and responsive styling
- **JavaScript** — browser-side interactions where implemented
- **Python `secrets` module** — recommended for security-sensitive random generation
- **Python `string` module** — character groups, if used by the implementation

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
password_generator/
├── manage.py
├── requirements.txt
├── config/
├── passwords/
├── templates/
├── static/
└── README.md
```

- `manage.py` — Django command-line utility used to run the application.
- `config/` — project settings and URL configuration.
- `passwords/` — password-generation application logic.
- `templates/` — Django HTML templates.
- `static/` — CSS, JavaScript, and other static assets.
- `requirements.txt` — Python dependencies.

## Concepts Practised

- Python functions and string manipulation
- Character sets and password composition
- Secure random generation with `secrets`, when implemented
- Input validation and conditional logic
- Django views, URL routing, and templates
- HTML form controls
- CSS layout and responsive design
- JavaScript interactions, such as copying to clipboard if implemented

## Learning Outcome

This project demonstrates how a Python utility can be exposed through a web interface. It combines configurable inputs, validation, password-generation logic, Django request handling, and frontend interaction.

## Security Notes

- Avoid logging generated passwords.
- Do not store generated passwords unless there is a clear, secure requirement.
- Use a cryptographically secure random source such as Python's `secrets` module for passwords.
- A password generator does not replace secure password storage or a reputable password manager.

## Notes

Run this project independently from the other applications. Each application has its own Django configuration and should be started from its own project directory.
