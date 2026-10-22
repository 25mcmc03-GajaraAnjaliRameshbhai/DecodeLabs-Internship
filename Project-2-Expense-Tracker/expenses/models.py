from django.db import models

class Expense(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.CharField(max_length=180, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.amount} - {self.note}"
