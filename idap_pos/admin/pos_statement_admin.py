from django.contrib import admin

from ..models import PosStatement


@admin.register(PosStatement)
class PosStatementAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "merchant",
                    "tran_date",
                    "transaction_time",
                    "date_transferred",
                    "pos_number",
                    "location",
                    "card_number",
                    "currency",
                    "gross_value",
                    "commission",
                    "net_value",
                ),
            },
        ),
        # audit_fieldset_tuple,
    )

    list_display = (
        "merchant",
        "tran_date",
        "transaction_time",
        "date_transferred",
        "pos_number",
        "location",
        "card_number",
        "currency",
        "gross_value",
        "commission",
        "net_value",
    )

    search_fields = (
        "merchant",
        "pos_number",
        "tran_date",
    )
