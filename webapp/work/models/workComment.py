from core.models import TimeStampModel
from django.db import models


class WorkComment(TimeStampModel):
    SCORE_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    class Meta:
        db_table = 'work comment'
        verbose_name = 'Work Comment'
        verbose_name_plural = 'Works Comment'

    work = models.ForeignKey(
        'work.Work',
        on_delete=models.CASCADE,
    )
    writer = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
    comment = models.TextField(
        verbose_name='댓글',
    )
    score = models.IntegerField(
        verbose_name="외주 평점",
        choices=SCORE_CHOICE,
        default=3,
        null=False,
    )