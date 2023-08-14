from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import Merchant


@admin.register(Merchant)
class MerchantAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "mid",
                    "frequency",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "name",
        "mid",
        "frequency",
    )

    search_fields = (
        "name",
        "mid",
        "frequency",
    )

    radio_fields = {
        "frequency": admin.VERTICAL,
    }
