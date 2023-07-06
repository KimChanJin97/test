# Generated by Django 4.2.2 on 2023-07-06 05:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Outsourcing',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='외주 고유번호')),
                ('field', models.CharField(choices=[(0, 'FRONTEND'), (1, 'HOMEPAGE'), (2, 'APPLICATION'), (3, 'GAME'), (4, 'BACKEND'), (5, 'DATA'), (6, 'WEB_MOBILE_DESIGN'), (7, 'VISUAL_DESIGN'), (8, 'LOGO_BRAND_DESIGN'), (9, 'PACKAGE_DESIGN'), (10, 'PRODUCT_DESIGN'), (11, 'CONSTRUCTION_DESIGN'), (12, 'INTERIOR_DESIGN'), (13, 'EXHIBITION_DESIGN'), (14, 'FASHION_DESIGN'), (15, 'JEWERLY_DESIGN'), (16, 'FABRIC_DESIGN'), (17, 'INDUSTRIAL_DESIGN'), (18, 'MEDIA_DESIGN'), (19, 'MOTION_GRAPHIC'), (20, 'FINE_ART')], max_length=500, verbose_name='외주 분야')),
                ('original_file_provided', models.BooleanField(verbose_name='원본파일제공여부')),
                ('commercial_use_allowed', models.BooleanField(verbose_name='상업적이용여부')),
                ('additional_modification_allowed', models.BooleanField(verbose_name='추가수정여부')),
                ('reprocessing_allowed', models.BooleanField(verbose_name='재가공여부')),
                ('work_date', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(90)], verbose_name='작업 예상일')),
                ('price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='금액')),
                ('editable_count', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], validators=[django.core.validators.MinValueValidator(0)], verbose_name='수정가능횟수')),
                ('price_change_allowed', models.BooleanField(verbose_name='가격변동가능여부')),
                ('outsourcing_method', models.CharField(max_length=30, null=True, verbose_name='작업 방식')),
                ('promotion_text', models.TextField(verbose_name='외주 홍보글')),
            ],
            options={
                'verbose_name': 'Outsourcing',
                'verbose_name_plural': 'Outsourcing',
                'db_table': 'outsourcing',
            },
        ),
        migrations.CreateModel(
            name='OutsourcingComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='외주 댓글 고유번호')),
                ('comment', models.TextField(verbose_name='댓글')),
                ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='외주 평점')),
                ('outsourcing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outsourcing.outsourcing', verbose_name='외주')),
            ],
            options={
                'verbose_name': 'Outsourcing Comment',
                'verbose_name_plural': 'Outsourcing Comments',
                'db_table': 'outsourcing comment',
            },
        ),
    ]
