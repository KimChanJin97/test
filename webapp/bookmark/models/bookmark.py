import uuid

from django.db import models

from core.models import TimeStampModel


class Bookmark(TimeStampModel):
    class Meta:
        db_table = 'bookmark'
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'

    uuid = models.UUIDField(
        verbose_name="북마크 고유번호",
        primary_key=True,
        null=False,
        default=uuid.uuid4
    )
    user = models.ForeignKey(
        'user.User',
        verbose_name="유저",
        on_delete=models.CASCADE,
        null=False,
    )
    work = models.ForeignKey(
        'work.Work',
        verbose_name='북마크 작업물',
        on_delete=models.CASCADE,
        null=False,
    )
