from django.db import models
from simple_history.models import HistoricalRecords

from idap_constants.choices import REPORT_FREQUENCY
from somans_dashboard.mixin import BaseUuidModel


class Merchant(BaseUuidModel):
    name = models.CharField(
        verbose_name="Merchant Name",
        max_length=255,
    )
    mid = models.CharField(
        verbose_name="Merchant ID",
        max_length=16,
    )
    email = models.TextField(
        verbose_name="Merchant Email",
        help_text="For multiple emails use this format user1@email.com,user2@email.com,user3@emai.com etc"
    )
    frequency = models.CharField(
        verbose_name="Report Frequency",
        max_length=16,
        choices=REPORT_FREQUENCY,

    )
    active = models.BooleanField(
        verbose_name="Activate report schedule",
        default=False
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Merchant"
        verbose_name_plural = "Merchant"
