# Generated by Django 4.1 on 2023-08-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Logs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("project_name", models.CharField(max_length=45, verbose_name="Project Name")),
                ("report_tag", models.CharField(max_length=16, verbose_name="Project Tag")),
                ("report_date", models.DateField(verbose_name="Report Date")),
                ("status", models.CharField(max_length=16, verbose_name="Status")),
                ("job_date", models.DateField(verbose_name="Job Date")),
                ("job_timestamp", models.DateTimeField(verbose_name="Job Timestamp")),
                ("job_output", models.TextField(verbose_name="Job Output")),
            ],
            options={
                "verbose_name": "IDAP Logs",
                "verbose_name_plural": "IDAP Logs",
            },
        ),
    ]
