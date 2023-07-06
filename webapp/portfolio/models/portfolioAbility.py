from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
import uuid

class PortfolioAbility(models.Model):
    class Meta:
        db_table = 'portfolio ability'
        verbose_name = 'Portfolio Ability'
        verbose_name_plural = 'Portfolio Abilities'

    uuid = models.UUIDField(
        verbose_name="포트폴리오 타임라인 고유번호",
        primary_key=True,
        null=False,
        default=uuid.uuid4
    )
    portfolio = models.ForeignKey(
        'portfolio.Portfolio',
        verbose_name='포트폴리오',
        on_delete=models.CASCADE,
        null=False,
    )
    ability = models.CharField(
        verbose_name='기술',
        max_length=10,
        null=False,
    )
    mastery = models.IntegerField(
        verbose_name='숙련도',
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        null=False,
    )
