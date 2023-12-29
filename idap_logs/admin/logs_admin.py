from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from ..models import Logs


@admin.register(Logs)
class LogsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
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

    list_filter = (
        "project_name",
        "report_tag",
        "status",
        "report_date",
        "job_date",
    )

    search_fields = (
        "project_name",
        "report_tag",
        "report_date",
        "job_date",
        "job_timestamp",
        "job_output",
    )
