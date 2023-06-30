from django.db import models


class Portfolio(models.Model):
    class Meta:
        db_table = 'portfolio'
        verbose_name = 'Portfolio'
        verbose_name_plural = 'Portfolios'

    user = models.OneToOneField(
        'user.User',
        verbose_name="유저",
        on_delete=models.CASCADE,
        null=False,
    )

    representative_image = models.ImageField(
        verbose_name='대표 이미지',
        null=True,
        upload_to='portfolio',
    )

    description = models.TextField(
        verbose_name='포트폴리오 설명',
        null=True,
        default="없음",
    )

    certification = models.CharField(
        verbose_name='자격증',
        max_length=100,
        null=True,
        default="없음"
    )

    career = models.CharField(
        verbose_name='경력',
        max_length=100,
        null=True,
        default="없음"
    )

    git = models.CharField(
        verbose_name='깃허브 링크',
        max_length=100,
        null=True,
        default="없음"
    )

    instagram = models.CharField(
        verbose_name='인스타그램 링크',
        max_length=100,
        null=True,
        default="없음"
    )

    twitter = models.CharField(
        verbose_name='트위터 링크',
        max_length=100,
        null=True,
        default="없음"
    )