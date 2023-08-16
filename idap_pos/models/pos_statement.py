from django.db import models
from django.utils import timezone


class PosStatement(models.Model):
    merchant = models.CharField(
        verbose_name="Merchant",
        max_length=255,
    )
    tran_date = models.CharField(
        verbose_name="Transaction Date",
        max_length=40,
    )
    transaction_time = models.CharField(
        verbose_name="Transaction Time",
        max_length=40,
    )
    date_transferred = models.CharField(
        verbose_name="Date Transferred",
        max_length=40,
    )
    pos_number = models.CharField(
        verbose_name="POS Number",
        max_length=16,
    )
    location = models.TextField(
        verbose_name="Location",
    )
    card_number = models.CharField(
        verbose_name="Card Number",
        max_length=40,
    )
    currency = models.CharField(
        verbose_name="Currency",
        max_length=10,
    )
    gross_value = models.CharField(
        verbose_name="Gross Value",
        max_length=40,
    )
    commission = models.CharField(
        verbose_name="Commission",
        max_length=40,
    )
    net_value = models.CharField(
        verbose_name="Net Value",
        max_length=40,
    )
    job_date = models.DateField(
        verbose_name="Job Date",
        default=timezone.now
    )
    job_timestamp = models.DateTimeField(
        verbose_name="Job Timestamp",
        default=timezone.now
    )

    def __str__(self):
        return self.merchant

    class Meta:
        verbose_name = "POS Statement"
        verbose_name_plural = "POS Statement"
