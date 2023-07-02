from django.db import models

from core.models import TimeStampModel


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
