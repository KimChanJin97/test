from django.db import models
from core.models import TimeStampModel


class OutsourcingComment(TimeStampModel):
    SCORE_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    class Meta:
        db_table = 'outsourcing comment'
        verbose_name = 'Outsourcing Comment'
        verbose_name_plural = 'Outsourcing Comments'

    outsourcing = models.ForeignKey(
        'outsourcing.Outsourcing',
        verbose_name="외주",
        on_delete=models.CASCADE,
        null=False,
    )

    writer = models.ForeignKey(
        'user.User',
        verbose_name="댓글 작성자",
        on_delete=models.CASCADE,
        null=False,
    )

    comment = models.TextField(
        verbose_name="댓글",
        null=False,
    )

    score = models.IntegerField(
        verbose_name="외주 평점",
        choices=SCORE_CHOICE,
        default=3,
        null=False,
    )