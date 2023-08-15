from django.contrib import admin

from ..models import Logs


@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "project_name",
                    "report_tag",
                    "report_date",
                    "status",
                    "job_date",
                    "job_timestamp",
                    "job_output",
                ),
            },
        ),
    )

    list_display = (
        "project_name",
        "report_tag",
        "report_date",
        "status",
        "job_date",
        "job_timestamp",
        "job_output",
    )

    search_fields = (
        "project_name",
        "report_tag",
        "report_date",
        "job_date",
        "job_timestamp",
        "job_output",
    )
