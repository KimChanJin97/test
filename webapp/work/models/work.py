from django.db import models

from core.models import TimeStampModel

FRONTEND = 0
HOMEPAGE = 1
APPLICATION = 2
GAME = 3
BACKEND = 4
DATA = 5
WEB_MOBILE_DESIGN = 6
VISUAL_DESIGN = 7
LOGO_BRAND_DESIGN = 8
PACKAGE_DESIGN = 9
PRODUCT_DESIGN = 10
CONSTRUCTION_DESIGN = 11
INTERIOR_DESIGN = 12
EXHIBITION_DESIGN = 13
FASHION_DESIGN = 14
JEWERLY_DESIGN = 15
FABRIC_DESIGN = 16
INDUSTRIAL_DESIGN = 17
MEDIA_DESIGN = 18
MOTION_GRAPHIC = 19
FINE_ART = 20

INTERESTS = ((FRONTEND, 'FRONTEND'),
            (HOMEPAGE, 'HOMEPAGE'),
            (APPLICATION, 'APPLICATION'),
            (GAME, 'GAME'),
            (BACKEND, 'BACKEND'),
            (DATA, 'DATA'),
            (WEB_MOBILE_DESIGN, 'WEB_MOBILE_DESIGN'),
            (VISUAL_DESIGN, 'VISUAL_DESIGN'),
            (LOGO_BRAND_DESIGN, 'LOGO_BRAND_DESIGN'),
            (PACKAGE_DESIGN, 'PACKAGE_DESIGN'),
            (PRODUCT_DESIGN, 'PRODUCT_DESIGN'),
            (CONSTRUCTION_DESIGN, 'CONSTRUCTION_DESIGN'),
            (INTERIOR_DESIGN, 'INTERIOR_DESIGN'),
            (EXHIBITION_DESIGN, 'EXHIBITION_DESIGN'),
            (FASHION_DESIGN, 'FASHION_DESIGN'),
            (JEWERLY_DESIGN, 'JEWERLY_DESIGN'),
            (FABRIC_DESIGN, 'FABRIC_DESIGN'),
            (INDUSTRIAL_DESIGN, 'INDUSTRIAL_DESIGN'),
            (MEDIA_DESIGN, 'MEDIA_DESIGN'),
            (MOTION_GRAPHIC, 'MOTION_GRAPHIC'),
            (FINE_ART, 'FINE_ART'),
            )


class Work(TimeStampModel):
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
    field = models.CharField(
        choices=INTERESTS,
        verbose_name="작업 분야",
        max_length=20,
        null=False,
    )
    description = models.TextField(
        verbose_name='작업물 설명',
        null=False,
        max_length=300,
    )

def image_upload_path(instance, filename):
    return f'{instance.work.portfolio.user.email}/{filename}'


class WorkImage(models.Model):
    work = models.ForeignKey(
        'work.Work',
        on_delete=models.CASCADE,
        related_name='image'
    )
    image = models.ImageField(
        upload_to=image_upload_path
    )