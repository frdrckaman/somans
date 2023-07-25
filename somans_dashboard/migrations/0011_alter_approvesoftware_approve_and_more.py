# Generated by Django 4.1 on 2023-07-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("somans_dashboard", "0010_approvesoftware_approve_review_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="approvesoftware",
            name="approve",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Approve"
            ),
        ),
        migrations.AlterField(
            model_name="approvesoftware",
            name="requester",
            field=models.CharField(default="A248080", max_length=10, verbose_name="Requester"),
        ),
        migrations.AlterField(
            model_name="historicalapprovesoftware",
            name="approve",
            field=models.CharField(
                blank=True, max_length=10, null=True, verbose_name="Approve"
            ),
        ),
        migrations.AlterField(
            model_name="historicalapprovesoftware",
            name="requester",
            field=models.CharField(default="A248080", max_length=10, verbose_name="Requester"),
        ),
    ]