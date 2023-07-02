from core.models import TimeStampModel
from django.db import models


class WorkComment(TimeStampModel):
    class Meta:
        db_table = 'work comment'
        verbose_name = 'Work Comment'
        verbose_name_plural = 'Works Comment'

    work = models.ForeignKey(
        'work.Work',
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        verbose_name='댓글'
    )