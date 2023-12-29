# Generated by Django 4.1 on 2023-09-04 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("idap_pos", "0002_alter_historicalmerchant_email_alter_merchant_email"),
    ]

    operations = [
        migrations.AddField(
            model_name="historicalmerchant",
            name="active",
            field=models.BooleanField(default=False, verbose_name="Activate report schedule"),
        ),
        migrations.AddField(
            model_name="merchant",
            name="active",
            field=models.BooleanField(default=False, verbose_name="Activate report schedule"),
        ),
    ]
