import getpass
from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords

from idap_dap.choices import DC_LOCATION
from somans_dashboard.mixin import BaseUuidModel


class DataCenterAccessRequest(BaseUuidModel):
    location = models.CharField(
        verbose_name="Location",
        choices=DC_LOCATION,
        max_length=30,
    )
    visitor_name = models.CharField(
        verbose_name="Visitor Name",
        max_length=40,
    )
    visitor_org = models.CharField(
        verbose_name="Visitor Organisation",
        max_length=40,
    )
    visitor_phone = models.CharField(
        verbose_name="Visitor Phone Number",
        max_length=40,
    )
    visitor_email = models.CharField(
        verbose_name="Visitor Email Address",
        max_length=40,
    )
    visitor_address = models.CharField(
        verbose_name="Visitor Address",
        max_length=40,
    )
    start_date = models.DateField(
        verbose_name="Start Date",
    )
    start_time = models.TimeField(
        verbose_name="Start Time",
    )
    end_date = models.DateField(
        verbose_name="End Date",
    )
    end_time = models.TimeField(
        verbose_name="End Time",
    )
    reason = models.TextField(
        verbose_name="Reasons",
    )
    requester = models.CharField(
        verbose_name="Requester",
        max_length=10,
        default=getpass.getuser(),
    )
    approver = models.CharField(
        verbose_name="Approver",
        max_length=40,
        blank=True,
        null=True,
    )
    approval_date = models.DateTimeField(
        verbose_name="Approval",
        blank=True,
        null=True,
    )
    approval_comment = models.TextField(
        verbose_name="Approval Comments",
        blank=True,
        null=True,
    )
    request_timestamp = models.DateTimeField(
        verbose_name="Request Timestamp",
        default=timezone.now,
    )
    status = models.IntegerField(
        verbose_name="Status",
        default=0
    )

    history = HistoricalRecords()

    def __str__(self):
        return self.visitor_name

    class Meta(BaseUuidModel.Meta):
        verbose_name = "Data Center Access Request"
        verbose_name_plural = "Data Center Access Request"
