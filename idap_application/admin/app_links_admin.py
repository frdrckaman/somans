from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import ApplicationLinks


@admin.register(ApplicationLinks)
class ApplicationLinksAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "app_name",
                    "app_env",
                    "app_link",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "app_name",
        "app_env",
        "app_link",
    )

    search_fields = (
        "app_name",
        "app_env",
    )

    radio_fields = {
        "app_env": admin.VERTICAL,
    }
