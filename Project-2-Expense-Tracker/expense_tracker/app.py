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
    db.execute("CREATE TABLE IF NOT EXISTS expenses_expense (id INTEGER PRIMARY KEY AUTOINCREMENT, amount DECIMAL NOT NULL, note VARCHAR(180) NOT NULL DEFAULT '', created_at TEXT NOT NULL)")


def index(request):
    with db_connection() as db:
        rows = db.execute("SELECT id, amount, note, created_at FROM expenses_expense ORDER BY id DESC").fetchall()
    expenses = []
    amounts = []
    for row in rows:
        item = dict(row)
        item["amount"] = Decimal(str(item["amount"]))
        try:
            item["created_at"] = datetime.fromisoformat(str(item["created_at"]))
        except ValueError:
            pass
        expenses.append(item)
        amounts.append(item["amount"])
    total = sum(amounts, Decimal("0.00"))
    count = len(amounts)
    summary = {"total": total, "average": total/count if count else Decimal("0.00"), "highest": max(amounts) if amounts else Decimal("0.00"), "lowest": min(amounts) if amounts else Decimal("0.00"), "count": count}
    return render(request, "index.html", {"expenses": expenses, "summary": summary})

@require_POST
def add(request):
    raw_amount = request.POST.get("amount", "").strip()
    note = request.POST.get("note", "").strip()[:180]
    try:
        amount = Decimal(raw_amount)
        if not amount.is_finite() or amount <= 0 or amount.as_tuple().exponent < -2 or amount > Decimal("9999999999.99"):
            raise InvalidOperation
    except (InvalidOperation, ValueError):
        messages.error(request, "Enter a valid positive amount with up to two decimal places.")
        return redirect("index")
    with db_connection() as db:
        db.execute("INSERT INTO expenses_expense (amount, note, created_at) VALUES (?, ?, ?)", (str(amount), note, datetime.now().isoformat(sep=" ", timespec="seconds")))
    messages.success(request, "Expense added successfully.")
    return redirect("index")

@require_POST
def delete(request, expense_id):
    with db_connection() as db:
        db.execute("DELETE FROM expenses_expense WHERE id = ?", (expense_id,))
    messages.success(request, "Expense deleted.")
    return redirect("index")

urlpatterns = [path("", index, name="index"), path("add/", add, name="add"), path("<int:expense_id>/delete/", delete, name="delete")]
