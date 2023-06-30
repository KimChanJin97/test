from django.db import models


class Field(models.Model):
    class Meta:
        db_table = "field"
        verbose_name = "Field"
        verbose_name_plural = "Fields"

    field = models.CharField(
        max_length=20
    )

    def __str__(self):
        return self.field

