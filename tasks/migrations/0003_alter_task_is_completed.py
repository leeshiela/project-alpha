# Generated by Django 5.0 on 2023-12-19 20:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0002_alter_task_is_completed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="is_completed",
            field=models.BooleanField(default=False),
        ),
    ]