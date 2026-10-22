from decimal import Decimal, InvalidOperation
from django.contrib import messages
from django.db.models import Sum, Avg, Max, Min, Count
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from .models import Expense


def index(request):
    expenses = Expense.objects.all()
    summary = expenses.aggregate(total=Sum("amount"), average=Avg("amount"), highest=Max("amount"), lowest=Min("amount"), count=Count("id"))
    summary["total"] = summary["total"] or Decimal("0.00")
    return render(request, "expenses/index.html", {"expenses": expenses, "summary": summary})

@require_POST
def add(request):
    raw_amount = request.POST.get("amount", "").strip()
    note = request.POST.get("note", "").strip()
    try:
        amount = Decimal(raw_amount)
        if not amount.is_finite() or amount <= 0:
            raise InvalidOperation
        if amount.as_tuple().exponent < -2:
            raise InvalidOperation
        if amount > Decimal("9999999999.99"):
            raise InvalidOperation
    except (InvalidOperation, ValueError):
        messages.error(request, "Enter a valid positive amount with up to two decimal places.")
        return redirect("expenses:index")
    Expense.objects.create(amount=amount, note=note[:180])
    messages.success(request, "Expense added successfully.")
    return redirect("expenses:index")

@require_POST
def delete(request, expense_id):
    Expense.objects.filter(pk=expense_id).delete()
    messages.success(request, "Expense deleted.")
    return redirect("expenses:index")
