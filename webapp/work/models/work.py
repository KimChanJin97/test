from django.db import models


class Work(models.Model):
    class Meta:
        db_table = 'work'
        verbose_name = 'Work'
        verbose_name_plural = 'Works'

    portfolio = models.ForeignKey(
        'portfolio.Portfolio',
        verbose_name="포트폴리오",
        on_delete=models.CASCADE,
        null=False,
    )
    field = models.ForeignKey(
        'field.Field',
        verbose_name="작업물 분야",
        on_delete=models.CASCADE,
        null=False,
    )
    description = models.TextField(
        verbose_name='작업물 설명',
        null=True,
        blank=True,
        max_length=300,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='작업물 생성 일시',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='작업물 수정 일시',
    )

    def __int__(self):
        return self.id


def image_upload_path(instance, filename):
    return f'{instance.work.portfolio.user.email}/{filename}'


class WorkImage(models.Model):
    id = models.AutoField(primary_key=True)
    work = models.ForeignKey('work.Work', on_delete=models.CASCADE, related_name='image')
    image = models.ImageField(upload_to=image_upload_path)


class WorkTag(models.Model):
    work = models.ForeignKey('work.Work', on_delete=models.CASCADE)
    tag = models.ForeignKey('tag.Tag', on_delete=models.CASCADE)

