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


class Outsourcing(TimeStampModel):
    EDITABLE_COUNT_CHOICE = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
        (9, "9"),
        (10, "10"),
    ]

    class Meta:
        db_table = 'outsourcing'
        verbose_name = 'Outsourcing'
        verbose_name_plural = 'Outsourcing'

    portfolio = models.ForeignKey(
        'portfolio.Portfolio',
        verbose_name="포트폴리오",
        on_delete=models.CASCADE,
        null=False,
    )
    field = models.CharField(
        choices=INTERESTS,
        verbose_name="외주 분야",
        max_length=500,
        null=False,
    )
    original_file_provided = models.BooleanField(
        verbose_name='원본파일제공여부',
        null=False,
    )
    commercial_use_allowed = models.BooleanField(
        verbose_name='상업적이용여부',
        null=False,
    )
    additional_modification_allowed = models.BooleanField(
        verbose_name='추가수정여부',
        null=False,
    )
    reprocessing_allowed = models.BooleanField(
        verbose_name='재가공여부',
        null=False,
    )
    work_date = models.PositiveIntegerField(
        verbose_name='작업 예상일',
        null=False,
    )
    price = models.IntegerField(
        verbose_name='금액',
        null=False,
    )
    editable_count = models.IntegerField(
        verbose_name='수정가능횟수',
        choices=EDITABLE_COUNT_CHOICE,
        null=False,
    )
    price_change_allowed = models.BooleanField(
        verbose_name='가격변동가능여부',
        null=False,
    )
    outsourcing_method = models.CharField(
        verbose_name='작업 방식',
        max_length=30,
        null=True,
    )
    promotion_text = models.TextField(
        verbose_name='외주 홍보글',
        null=False,
    )
