from django.db import models


class Bookmark(models.Model):
    class Meta:
        db_table = 'bookmark'
        verbose_name = 'Bookmark'
        verbose_name_plural = 'Bookmarks'

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
