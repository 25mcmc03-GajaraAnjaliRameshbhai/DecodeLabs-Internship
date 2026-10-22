# Generated for the Expense model.
from django.db import migrations, models

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [migrations.CreateModel(name="Expense", fields=[("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")), ("amount", models.DecimalField(decimal_places=2, max_digits=12)), ("note", models.CharField(blank=True, max_length=180)), ("created_at", models.DateTimeField(auto_now_add=True))], options={"ordering": ["-created_at"]}),]
