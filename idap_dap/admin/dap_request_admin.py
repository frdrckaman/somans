from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin as BaseSimpleHistoryAdmin

from ..models import DataCenterAccessRequest


@admin.register(DataCenterAccessRequest)
class DataCenterAccessRequestAdmin(BaseSimpleHistoryAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "location",
                    "visitor_name",
                    "visitor_org",
                    "visitor_phone",
                    "visitor_email",
                    "visitor_address",
                    "start_date",
                    "start_time",
                    "end_date",
                    "end_time",
                    "reason",
                    "requester",
                    "approver",
                    "approval_date",
                    "approval_comment",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "location",
        "visitor_name",
        "visitor_org",
        "visitor_phone",
        "start_date",
        "start_time",
        "end_date",
        "end_time",
    )

    search_fields = (
        "location",
        "visitor_name",
    )

    list_filter = (
        "location",
        "start_date",
        "end_date",
    )

    radio_fields = {
        "location": admin.VERTICAL,
    }
