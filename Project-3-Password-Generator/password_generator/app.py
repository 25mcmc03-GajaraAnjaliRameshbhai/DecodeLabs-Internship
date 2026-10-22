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

def index(request):
    password = None
    error = None
    length = 16
    if request.method == "POST":
        try:
            length = int(request.POST.get("length", "16"))
            if not 8 <= length <= 64:
                raise ValueError
            groups = []
            if request.POST.get("uppercase") == "on": groups.append(string.ascii_uppercase)
            if request.POST.get("lowercase") == "on": groups.append(string.ascii_lowercase)
            if request.POST.get("digits") == "on": groups.append(string.digits)
            if request.POST.get("symbols") == "on": groups.append(string.punctuation)
            if not groups:
                error = "Select at least one character type."
            elif length < len(groups):
                error = "Password length must be at least the number of selected character types."
            else:
                chars = [secrets.choice(group) for group in groups]
                pool = "".join(groups)
                chars.extend(secrets.choice(pool) for _ in range(length-len(chars)))
                secrets.SystemRandom().shuffle(chars)
                password = "".join(chars)
        except (TypeError, ValueError):
            error = "Choose a password length between 8 and 64."
            length = 16
    return render(request, "index.html", {"password": password, "error": error, "length": length})

urlpatterns = [path("", index, name="index")]
