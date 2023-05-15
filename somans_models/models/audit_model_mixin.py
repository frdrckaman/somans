import socket
from datetime import datetime

import arrow
from django.db import models


def utcnow() -> datetime:
    return arrow.utcnow().datetime


class AuditModelMixin(models.Model):

    """Base model class for all models. Adds created and modified'
    values for user, date and hostname (computer).
    """

    get_latest_by = "modified"

    created = models.DateTimeField(blank=True, default=utcnow)

    modified = models.DateTimeField(blank=True, default=utcnow)

    hostname_created = models.CharField(
        max_length=60,
        blank=True,
        default=socket.gethostname,
        help_text="System field. (modified on create only)",
    )

    device_created = models.CharField(max_length=10, blank=True)

    device_modified = models.CharField(max_length=10, blank=True)

    objects = models.Manager()

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    class Meta:
        get_latest_by = "modified"
        ordering = ("-modified", "-created")
        abstract = True
