from django.db import models
from simple_history.models import HistoricalRecords

from idap_application.choices import APP_ENV
from somans_dashboard.mixin import BaseUuidModel


class ApplicationLinks(BaseUuidModel):
    app_name = models.CharField(
        verbose_name="Application Name",
        max_length=40,
    )
    app_link = models.TextField(
        verbose_name="Application Link",
    )
    app_env = models.CharField(
        verbose_name="Application Environment",
        choices=APP_ENV,
        max_length=10,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.app_name

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Application Links"
        verbose_name_plural = "Application Links"
