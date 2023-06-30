from django.db import models


class Tag(models.Model):
    class Meta:
        db_table = "tag"
        verbose_name = "tag"
        verbose_name_plural = "tags"

    tag = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.tag

