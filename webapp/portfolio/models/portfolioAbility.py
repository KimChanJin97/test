from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class PortfolioAbility(models.Model):
    class Meta:
        db_table = 'ability'
        verbose_name = 'Ability'
        verbose_name_plural = 'Abilities'

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
