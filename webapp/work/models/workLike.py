import uuid

from django.db import models

from core.models import TimeStampModel


class WorkLike(TimeStampModel):
    class Meta:
        db_table = 'work like'
        verbose_name = 'Work Like'
        verbose_name_plural = 'Works Likes'

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
    liker = models.ForeignKey(
        'user.User',
        on_delete=models.CASCADE,
    )
