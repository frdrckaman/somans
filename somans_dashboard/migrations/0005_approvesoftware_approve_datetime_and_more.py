# Generated by Django 4.1 on 2023-07-17 11:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("somans_dashboard", "0004_alter_approvesoftware_requester_date_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="approvesoftware",
            name="approve_datetime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Approve Date"
            ),
        ),
        migrations.AddField(
            model_name="approvesoftware",
            name="requester_datetime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Requester Date"
            ),
        ),
        migrations.AddField(
            model_name="approvesoftware",
            name="status",
            field=models.IntegerField(blank=True, null=True, verbose_name="Status"),
        ),
        migrations.AddField(
            model_name="historicalapprovesoftware",
            name="approve_datetime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Approve Date"
            ),
        ),
        migrations.AddField(
            model_name="historicalapprovesoftware",
            name="requester_datetime",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Requester Date"
            ),
        ),
        migrations.AddField(
            model_name="historicalapprovesoftware",
            name="status",
            field=models.IntegerField(blank=True, null=True, verbose_name="Status"),
        ),
    ]