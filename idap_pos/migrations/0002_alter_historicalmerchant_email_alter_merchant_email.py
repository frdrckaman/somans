# Generated by Django 4.1 on 2023-08-17 05:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("idap_pos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalmerchant",
            name="email",
            field=models.TextField(
                help_text="For multiple emails use this format user1@email.com,user2@email.com,user3@emai.com etc",
                verbose_name="Merchant Email",
            ),
        ),
        migrations.AlterField(
            model_name="merchant",
            name="email",
            field=models.TextField(
                help_text="For multiple emails use this format user1@email.com,user2@email.com,user3@emai.com etc",
                verbose_name="Merchant Email",
            ),
        ),
    ]