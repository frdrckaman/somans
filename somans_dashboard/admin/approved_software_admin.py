from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import ApproveSoftware


@admin.register(ApproveSoftware)
class ApproveSoftwareAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "product_name",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "product_name",
    )

    search_fields = (
        "product_name",
    )
