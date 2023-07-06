import uuid

from django.db import models

from core.choices import INTERESTS
from core.models import TimeStampModel


class Work(TimeStampModel):
    class Meta:
        db_table = 'work'
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    uuid = models.UUIDField(
        verbose_name="작업물 고유번호",
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
    field = models.CharField(
        choices=INTERESTS,
        verbose_name="작업 분야",
        max_length=500,
        null=False,
    )
    description = models.TextField(
        verbose_name='작업물 설명',
        null=False,
        max_length=300,
    )
    likes = models.ManyToManyField(
        'user.User',
        related_name='like_works'
    )


def image_upload_path(instance, filename):
    return f'{instance.work.portfolio.user.email}/{filename}'


class WorkImage(models.Model):
    work = models.ForeignKey(
        'work.Work',
        on_delete=models.CASCADE,
        related_name='image'
    )
    image = models.ImageField(
        upload_to=image_upload_path
    )
