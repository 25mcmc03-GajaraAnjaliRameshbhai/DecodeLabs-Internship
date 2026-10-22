from pathlib import Path
import sqlite3
import secrets
import string
from decimal import Decimal, InvalidOperation
from datetime import datetime
from contextlib import contextmanager

# Django settings and URL routes live in this one file to keep the project compact.
BASE_DIR = Path(__file__).resolve().parent
SECRET_KEY = "local-development-key-for-local-use-only"
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "testserver"]
ROOT_URLCONF = "app"
INSTALLED_APPS = ["django.contrib.staticfiles", "django.contrib.messages"]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR],
    "APP_DIRS": False,
    "OPTIONS": {"context_processors": ["django.contrib.messages.context_processors.messages"]},
}]
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

from django.contrib import messages
from django.http import HttpResponseNotAllowed
from django.shortcuts import redirect, render
from django.urls import path
from django.views.decorators.http import require_POST


@contextmanager
def db_connection():
    connection = sqlite3.connect(BASE_DIR / "db.sqlite3")
    connection.row_factory = sqlite3.Row
    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()


with db_connection() as db:
    db.execute("CREATE TABLE IF NOT EXISTS tasks_task (id INTEGER PRIMARY KEY AUTOINCREMENT, title VARCHAR(240) NOT NULL, completed INTEGER NOT NULL DEFAULT 0, created_at TEXT NOT NULL)")


def index(request):
    query = request.GET.get("q", "").strip()
    with db_connection() as db:
        if query:
            rows = db.execute("SELECT id, title, completed, created_at FROM tasks_task WHERE title LIKE ? COLLATE NOCASE ORDER BY id DESC", (f"%{query}%",)).fetchall()
        else:
            rows = db.execute("SELECT id, title, completed, created_at FROM tasks_task ORDER BY id DESC").fetchall()
        total = db.execute("SELECT COUNT(*) FROM tasks_task").fetchone()[0]
        completed = db.execute("SELECT COUNT(*) FROM tasks_task WHERE completed = 1").fetchone()[0]
    tasks = [dict(row) for row in rows]
    return render(request, "index.html", {"tasks": tasks, "query": query, "total": total, "completed": completed, "pending": total-completed})

@require_POST
def add(request):
    title = request.POST.get("title", "").strip()
    if not title:
        messages.error(request, "Task cannot be empty.")
    else:
        with db_connection() as db:
            db.execute("INSERT INTO tasks_task (title, completed, created_at) VALUES (?, 0, ?)", (title[:240], datetime.now().isoformat(sep=" ", timespec="seconds")))
        messages.success(request, "Task added.")
    return redirect("index")

@require_POST
def toggle(request, task_id):
    with db_connection() as db:
        db.execute("UPDATE tasks_task SET completed = CASE completed WHEN 1 THEN 0 ELSE 1 END WHERE id = ?", (task_id,))
    return redirect("index")

@require_POST
def delete(request, task_id):
    with db_connection() as db:
        db.execute("DELETE FROM tasks_task WHERE id = ?", (task_id,))
    messages.success(request, "Task deleted.")
    return redirect("index")

urlpatterns = [path("", index, name="index"), path("add/", add, name="add"), path("<int:task_id>/toggle/", toggle, name="toggle"), path("<int:task_id>/delete/", delete, name="delete")]
