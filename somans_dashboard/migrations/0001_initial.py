# Generated by Django 4.1 on 2023-07-28 08:46

import _socket
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import simple_history.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ApproveSoftware",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "product_name",
                    models.CharField(max_length=255, verbose_name="Product Name"),
                ),
                (
                    "requester",
                    models.CharField(
                        default="A248080", max_length=10, verbose_name="Requester"
                    ),
                ),
                (
                    "requester_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Requester Date"
                    ),
                ),
                (
                    "requester_datetime",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Requester Date"
                    ),
                ),
                (
                    "approve",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Approve"
                    ),
                ),
                (
                    "approve_date",
                    models.DateField(blank=True, null=True, verbose_name="Approve date"),
                ),
                (
                    "approve_datetime",
                    models.DateTimeField(blank=True, null=True, verbose_name="Approve Date"),
                ),
                (
                    "devices_permitted",
                    models.CharField(
                        blank=True,
                        max_length=4,
                        null=True,
                        verbose_name="Have you review all devices which this software is installed and ensure that they have permission to use this product?",
                    ),
                ),
                (
                    "approve_review",
                    models.CharField(
                        blank=True,
                        max_length=4,
                        null=True,
                        verbose_name="Did you briefly review this request?",
                    ),
                ),
                ("status", models.IntegerField(default=0, verbose_name="Status")),
                (
                    "reasons",
                    models.TextField(
                        blank=True, null=True, verbose_name="Reasons for this request"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, null=True, verbose_name="Additional Comments"
                    ),
                ),
                (
                    "next_url_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Redirect to?"
                    ),
                ),
            ],
            options={
                "verbose_name": "Approve Software",
                "verbose_name_plural": "Approve Software",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.CreateModel(
            name="AppTheme",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "theme_mode",
                    models.CharField(
                        choices=[("dark", "Dark Mode"), ("light", "Light Mode")],
                        default="light",
                        max_length=8,
                        verbose_name="Theme",
                    ),
                ),
                (
                    "theme_name",
                    models.CharField(
                        default="Dark Mode", max_length=24, verbose_name="Theme Name"
                    ),
                ),
                (
                    "theme_user",
                    models.CharField(
                        blank=True, max_length=12, null=True, verbose_name="Username"
                    ),
                ),
            ],
            options={
                "verbose_name": "App Theme",
                "verbose_name_plural": "App Theme",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.CreateModel(
            name="HistoricalAppTheme",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "theme_mode",
                    models.CharField(
                        choices=[("dark", "Dark Mode"), ("light", "Light Mode")],
                        default="light",
                        max_length=8,
                        verbose_name="Theme",
                    ),
                ),
                (
                    "theme_name",
                    models.CharField(
                        default="Dark Mode", max_length=24, verbose_name="Theme Name"
                    ),
                ),
                (
                    "theme_user",
                    models.CharField(
                        blank=True, max_length=12, null=True, verbose_name="Username"
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical App Theme",
                "verbose_name_plural": "historical App Theme",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name="HistoricalApproveSoftware",
            fields=[
                (
                    "revision",
                    django_revision.revision_field.RevisionField(
                        blank=True,
                        editable=False,
                        help_text="System field. Git repository tag:branch:commit.",
                        max_length=75,
                        null=True,
                        verbose_name="Revision",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "modified",
                    models.DateTimeField(
                        blank=True, default=django_audit_fields.models.audit_model_mixin.utcnow
                    ),
                ),
                (
                    "user_created",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user created",
                    ),
                ),
                (
                    "user_modified",
                    django_audit_fields.fields.userfield.UserField(
                        blank=True,
                        help_text="Updated by admin.save_model",
                        max_length=50,
                        verbose_name="user modified",
                    ),
                ),
                (
                    "hostname_created",
                    models.CharField(
                        blank=True,
                        default=_socket.gethostname,
                        help_text="System field. (modified on create only)",
                        max_length=60,
                    ),
                ),
                (
                    "hostname_modified",
                    django_audit_fields.fields.hostname_modification_field.HostnameModificationField(
                        blank=True,
                        help_text="System field. (modified on every save)",
                        max_length=50,
                    ),
                ),
                ("device_created", models.CharField(blank=True, max_length=10)),
                ("device_modified", models.CharField(blank=True, max_length=10)),
                (
                    "id",
                    django_audit_fields.fields.uuid_auto_field.UUIDAutoField(
                        blank=True,
                        db_index=True,
                        editable=False,
                        help_text="System auto field. UUID primary key.",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(max_length=255, verbose_name="Product Name"),
                ),
                (
                    "requester",
                    models.CharField(
                        default="A248080", max_length=10, verbose_name="Requester"
                    ),
                ),
                (
                    "requester_date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="Requester Date"
                    ),
                ),
                (
                    "requester_datetime",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Requester Date"
                    ),
                ),
                (
                    "approve",
                    models.CharField(
                        blank=True, max_length=10, null=True, verbose_name="Approve"
                    ),
                ),
                (
                    "approve_date",
                    models.DateField(blank=True, null=True, verbose_name="Approve date"),
                ),
                (
                    "approve_datetime",
                    models.DateTimeField(blank=True, null=True, verbose_name="Approve Date"),
                ),
                (
                    "devices_permitted",
                    models.CharField(
                        blank=True,
                        max_length=4,
                        null=True,
                        verbose_name="Have you review all devices which this software is installed and ensure that they have permission to use this product?",
                    ),
                ),
                (
                    "approve_review",
                    models.CharField(
                        blank=True,
                        max_length=4,
                        null=True,
                        verbose_name="Did you briefly review this request?",
                    ),
                ),
                ("status", models.IntegerField(default=0, verbose_name="Status")),
                (
                    "reasons",
                    models.TextField(
                        blank=True, null=True, verbose_name="Reasons for this request"
                    ),
                ),
                (
                    "comment",
                    models.TextField(
                        blank=True, null=True, verbose_name="Additional Comments"
                    ),
                ),
                (
                    "next_url_name",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Redirect to?"
                    ),
                ),
                ("history_id", models.AutoField(primary_key=True, serialize=False)),
                ("history_date", models.DateTimeField(db_index=True)),
                ("history_change_reason", models.CharField(max_length=100, null=True)),
                (
                    "history_type",
                    models.CharField(
                        choices=[("+", "Created"), ("~", "Changed"), ("-", "Deleted")],
                        max_length=1,
                    ),
                ),
                (
                    "history_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "historical Approve Software",
                "verbose_name_plural": "historical Approve Software",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
