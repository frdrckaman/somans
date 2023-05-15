from django.db import models
from somans_models.models import AuditModelMixin


class Headcount(AuditModelMixin):
    personnel_number = models.CharField(
        verbose_name="Personnel number",
        max_length=45,
        null=True,
    )

    last_name = models.CharField(
        verbose_name="Lastname",
        max_length=45,
        null=True,
    )

    first_name = models.CharField(
        verbose_name="Firstname",
        max_length=45,
        null=True,
    )

    personnel_area_text = models.CharField(
        verbose_name="Personnel Area text",
        max_length=45,
        null=True,
    )

    name_of_ee_subgroup = models.CharField(
        verbose_name="Name of EE subgroup",
        max_length=45,
        null=True,
    )
    cost_center = models.CharField(
        verbose_name="Cost center",
        max_length=15,
        null=True,
    )
    cost_center_name = models.CharField(
        verbose_name="Cost center name",
        max_length=45,
        null=True,
    )

    class Meta:
        verbose_name = "Headcount"
        verbose_name_plural = "Headcount"
