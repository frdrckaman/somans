# Generated by Django 4.1 on 2023-09-29 12:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("idap_dap", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="datacenteraccessrequest",
            name="status",
            field=models.IntegerField(default=0, verbose_name="Status"),
        ),
        migrations.AddField(
            model_name="historicaldatacenteraccessrequest",
            name="status",
            field=models.IntegerField(default=0, verbose_name="Status"),
        ),
    ]