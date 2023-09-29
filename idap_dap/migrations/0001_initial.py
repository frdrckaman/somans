# Generated by Django 4.1 on 2023-09-29 09:57

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
            name="DataCenterAccessRequest",
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
                    "location",
                    models.CharField(
                        choices=[("on_premises", "On Premises"), ("dr", "On DR")],
                        max_length=30,
                        verbose_name="Location",
                    ),
                ),
                ("visitor_name", models.CharField(max_length=40, verbose_name="Visitor Name")),
                (
                    "visitor_org",
                    models.CharField(max_length=40, verbose_name="Visitor Organisation"),
                ),
                (
                    "visitor_phone",
                    models.CharField(max_length=40, verbose_name="Visitor Phone Number"),
                ),
                (
                    "visitor_email",
                    models.CharField(max_length=40, verbose_name="Visitor Email Address"),
                ),
                (
                    "visitor_address",
                    models.CharField(max_length=40, verbose_name="Visitor Address"),
                ),
                ("start_date", models.DateField(verbose_name="Start Date")),
                ("start_time", models.TimeField(verbose_name="Start Time")),
                ("end_date", models.DateField(verbose_name="End Date")),
                ("end_time", models.TimeField(verbose_name="End Time")),
                ("reason", models.TextField(verbose_name="Reasons")),
                (
                    "requester",
                    models.CharField(
                        default="A248080", max_length=10, verbose_name="Requester"
                    ),
                ),
                (
                    "approver",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="Approver"
                    ),
                ),
                (
                    "approval_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="Approval"),
                ),
                (
                    "approval_comment",
                    models.TextField(blank=True, null=True, verbose_name="Approval Comments"),
                ),
                (
                    "request_timestamp",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Request Timestamp"
                    ),
                ),
            ],
            options={
                "verbose_name": "Data Center Access Request",
                "verbose_name_plural": "Data Center Access Request",
                "ordering": ("-modified", "-created"),
                "get_latest_by": "modified",
                "abstract": False,
                "default_permissions": ("add", "change", "delete", "view", "export", "import"),
            },
        ),
        migrations.CreateModel(
            name="HistoricalDataCenterAccessRequest",
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
                    "location",
                    models.CharField(
                        choices=[("on_premises", "On Premises"), ("dr", "On DR")],
                        max_length=30,
                        verbose_name="Location",
                    ),
                ),
                ("visitor_name", models.CharField(max_length=40, verbose_name="Visitor Name")),
                (
                    "visitor_org",
                    models.CharField(max_length=40, verbose_name="Visitor Organisation"),
                ),
                (
                    "visitor_phone",
                    models.CharField(max_length=40, verbose_name="Visitor Phone Number"),
                ),
                (
                    "visitor_email",
                    models.CharField(max_length=40, verbose_name="Visitor Email Address"),
                ),
                (
                    "visitor_address",
                    models.CharField(max_length=40, verbose_name="Visitor Address"),
                ),
                ("start_date", models.DateField(verbose_name="Start Date")),
                ("start_time", models.TimeField(verbose_name="Start Time")),
                ("end_date", models.DateField(verbose_name="End Date")),
                ("end_time", models.TimeField(verbose_name="End Time")),
                ("reason", models.TextField(verbose_name="Reasons")),
                (
                    "requester",
                    models.CharField(
                        default="A248080", max_length=10, verbose_name="Requester"
                    ),
                ),
                (
                    "approver",
                    models.CharField(
                        blank=True, max_length=40, null=True, verbose_name="Approver"
                    ),
                ),
                (
                    "approval_date",
                    models.DateTimeField(blank=True, null=True, verbose_name="Approval"),
                ),
                (
                    "approval_comment",
                    models.TextField(blank=True, null=True, verbose_name="Approval Comments"),
                ),
                (
                    "request_timestamp",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="Request Timestamp"
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
                "verbose_name": "historical Data Center Access Request",
                "verbose_name_plural": "historical Data Center Access Request",
                "ordering": ("-history_date", "-history_id"),
                "get_latest_by": ("history_date", "history_id"),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
