from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import FinServicesTimer


@admin.register(FinServicesTimer)
class FinServicesTimerAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "last_run",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "last_run",
    )

    search_fields = (
        "last_run",
    )

    list_filter = (
        "last_run",
    )