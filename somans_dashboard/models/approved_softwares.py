import getpass
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from ..mixin import BaseUuidModel


class ApproveSoftware(BaseUuidModel):
    product_name = models.CharField(
        verbose_name="Product Name",
        max_length=255,
    )
    requester = models.CharField(
        verbose_name="Requester",
        max_length=20,
        default=getpass.getuser(),
    )
    requester_date = models.DateField(
        verbose_name="Requester Date",
        default=timezone.now,
    )
    requester_datetime = models.DateTimeField(
        verbose_name="Requester Date",
        default=timezone.now,
    )
    approve = models.CharField(
        verbose_name="Approve",
        max_length=4,
        blank=True,
        null=True,
    )
    approve_date = models.DateField(
        verbose_name="Approve date",
        blank=True,
        null=True,
    )
    approve_datetime = models.DateTimeField(
        verbose_name="Approve Date",
        blank=True,
        null=True,
    )
    status = models.IntegerField(
        verbose_name="Status",
        blank=True,
        null=True,
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.product_name

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Approve Software"
        verbose_name_plural = "Approve Software"
