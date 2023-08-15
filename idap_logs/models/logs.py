from django.db import models


class Logs(models.Model):
    project_name = models.CharField(
        verbose_name="Project Name",
        max_length=45,
    )
    report_tag = models.CharField(
        verbose_name="Project Tag",
        max_length=16,
    )
    report_date = models.DateField(
        verbose_name="Report Date",
    )
    status = models.CharField(
        verbose_name="Status",
        max_length=16
    )
    job_date = models.DateField(
        verbose_name="Job Date",
    )
    job_timestamp = models.DateTimeField(
        verbose_name="Job Timestamp",
    )
    job_output = models.TextField(
        verbose_name="Job Output",
    )

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = "IDAP Logs"
        verbose_name_plural = "IDAP Logs"