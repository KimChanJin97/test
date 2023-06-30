from django.db import models


class Outsourcing(models.Model):
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

    field = models.OneToOneField(
        'field.Field',
        verbose_name="외주 분야",
        on_delete=models.CASCADE,
        null=True,
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


