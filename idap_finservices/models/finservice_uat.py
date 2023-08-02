from django.db import models


class FinServicesUat(models.Model):
    ConfigService = models.CharField(
        verbose_name='ConfigService',
        max_length=6
    )
    FINRPT_finlstclnt = models.CharField(
        verbose_name='FINRPT-finlstclnt',
        max_length=6
    )
    FINRPT_comnclnt = models.CharField(
        verbose_name='FINRPT-comnclnt',
        max_length=6
    )
    CBC = models.CharField(
        verbose_name='CBC',
        max_length=6
    )
    Finlistval = models.CharField(
        verbose_name='Finlistval',
        max_length=6
    )
    Coresession = models.CharField(
        verbose_name='Coresession',
        max_length=6
    )
    Referral = models.CharField(
        verbose_name='Referral',
        max_length=6
    )
    Uniser_TZ = models.CharField(
        verbose_name='Uniser-TZ',
        max_length=6
    )
    MQMSwiftIn_TZ = models.CharField(
        verbose_name='MQMSwiftIn-TZ',
        max_length=6
    )
    MQMSwiftOut_TZ = models.CharField(
        verbose_name='MQMSwiftOut-TZ',
        max_length=6
    )
    MQMRtgsIn_TZ = models.CharField(
        verbose_name='MQMRtgsIn-TZ',
        max_length=6
    )
    MQMRtgsOut_TZ = models.CharField(
        verbose_name='MQMRtgsOut-TZ',
        max_length=6
    )
    MQMRead_TZ = models.CharField(
        verbose_name='MQMRead-TZ',
        max_length=6
    )
    Dispatcher_TZ = models.CharField(
        verbose_name='Dispatcher-TZ',
        max_length=6
    )
    Binagent_TZ = models.CharField(
        verbose_name='Binagent-TZ',
        max_length=6
    )
    Swiftsrv_TZ = models.CharField(
        verbose_name='Swiftsrv-TZ',
        max_length=6
    )
    Pmssrv_TZ = models.CharField(
        verbose_name='Pmssrv-TZ',
        max_length=6
    )
    Genlimo_TZ = models.CharField(
        verbose_name='Genlimo-TZ',
        max_length=6
    )
    Aabsrv_TZ = models.CharField(
        verbose_name='Aabsrv-TZ',
        max_length=6
    )
    Eabgst_TZ = models.CharField(
        verbose_name='Eabgst-TZ',
        max_length=6
    )
    Trswift_TZ = models.CharField(
        verbose_name='Trswift-TZ',
        max_length=6
    )
    Uplpsmsg_TZ = models.CharField(
        verbose_name='Uplpsmsg_TZ',
        max_length=6
    )
    fin_timestamp = models.CharField(
        verbose_name='Timestamp',
        max_length=45,
    )
    node = models.IntegerField(
        verbose_name='Node',
        default=0
    )
