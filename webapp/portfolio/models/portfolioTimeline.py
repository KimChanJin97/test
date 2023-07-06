import uuid

from django.db import models

from core.models import TimeStampModel


class PortfolioTimeline(TimeStampModel):
    class Meta:
        db_table = 'portfolio timeline'
        verbose_name = 'Portfolio Timeline'
        verbose_name_plural = 'Portfolio Timelines'

    uuid = models.UUIDField(
        verbose_name="포트폴리오 타임라인 고유번호",
        primary_key=True,
        null=False,
        default=uuid.uuid4
    )
    portfolio = models.ForeignKey(
        'portfolio.Portfolio',
        verbose_name="포트폴리오",
        on_delete=models.CASCADE,
        null=False,
    )
    year = models.CharField(
        verbose_name='년도',
        max_length=20,
        null=False,
    )
    description = models.CharField(
        verbose_name='설명',
        max_length=20,
        null=False,
    )
