import uuid

from django.db import models

from core.models import TimeStampModel


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
        verbose_name_plural = 'Works Comments'

    uuid = models.UUIDField(
        verbose_name="작업물 댓글 고유번호",
        primary_key=True,
        null=False,
        default=uuid.uuid4
    )
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
        verbose_name="작업물 평점",
        choices=SCORE_CHOICE,
        default=3,
        null=False,
    )