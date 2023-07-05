from django.db import models

from core.models import TimeStampModel
import uuid

class PortfolioComment(TimeStampModel):
    SCORE_CHOICE = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    class Meta:
        db_table = 'portfolio comment'
        verbose_name = 'Portfolio Comment'
        verbose_name_plural = 'Portfolio Comments'

    uuid = models.UUIDField(
        verbose_name="포트폴리오 댓글 고유번호",
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
        verbose_name="포트폴리오 평점",
        choices=SCORE_CHOICE,
        default=3,
        null=False,
    )
