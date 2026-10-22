from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import Task


def index(request):
    query = request.GET.get("q", "").strip()
    tasks = Task.objects.filter(Q(title__icontains=query)) if query else Task.objects.all()
    total = Task.objects.count()
    completed = Task.objects.filter(completed=True).count()
    return render(request, "tasks/index.html", {
        "tasks": tasks, "query": query, "total": total,
        "completed": completed, "pending": total - completed,
    })

@require_POST
def add(request):
    title = request.POST.get("title", "").strip()
    if not title:
        messages.error(request, "Task cannot be empty.")
    else:
        Task.objects.create(title=title)
        messages.success(request, "Task added.")
    return redirect("tasks:index")

@require_POST
def toggle(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.completed = not task.completed
    task.save(update_fields=["completed"])
    return redirect("tasks:index")

@require_POST
def delete(request, task_id):
    get_object_or_404(Task, pk=task_id).delete()
    messages.success(request, "Task deleted.")
    return redirect("tasks:index")
