from django.db import models

from somans_dashboard.mixin import BaseUuidModel


class FinServicesTimer(BaseUuidModel):
    last_run = models.DateTimeField(
        verbose_name='Last Run',
    )