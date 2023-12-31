# Generated by Django 4.2.2 on 2023-07-07 03:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import portfolio.models.portfolio
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='포트폴리오 고유번호')),
                ('representative_image', models.ImageField(null=True, upload_to=portfolio.models.portfolio.image_upload_path, verbose_name='대표 이미지')),
                ('description', models.TextField(default='없음', null=True, verbose_name='포트폴리오 설명')),
                ('certification', models.CharField(default='없음', max_length=100, null=True, verbose_name='자격증')),
                ('career', models.CharField(default='없음', max_length=100, null=True, verbose_name='경력')),
                ('git', models.CharField(default='없음', max_length=100, null=True, verbose_name='깃허브 링크')),
                ('instagram', models.CharField(default='없음', max_length=100, null=True, verbose_name='인스타그램 링크')),
                ('twitter', models.CharField(default='없음', max_length=100, null=True, verbose_name='트위터 링크')),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
                'db_table': 'portfolio',
            },
        ),
        migrations.CreateModel(
            name='PortfolioAbility',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='포트폴리오 타임라인 고유번호')),
                ('ability', models.CharField(max_length=10, verbose_name='기술')),
                ('mastery', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='숙련도')),
            ],
            options={
                'verbose_name': 'Portfolio Ability',
                'verbose_name_plural': 'Portfolio Abilities',
                'db_table': 'portfolio ability',
            },
        ),
        migrations.CreateModel(
            name='PortfolioTimeline',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='포트폴리오 타임라인 고유번호')),
                ('year', models.CharField(max_length=20, verbose_name='년도')),
                ('description', models.CharField(max_length=20, verbose_name='설명')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio', verbose_name='포트폴리오')),
            ],
            options={
                'verbose_name': 'Portfolio Timeline',
                'verbose_name_plural': 'Portfolio Timelines',
                'db_table': 'portfolio timeline',
            },
        ),
        migrations.CreateModel(
            name='PortfolioComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='포트폴리오 댓글 고유번호')),
                ('comment', models.TextField(verbose_name='댓글')),
                ('score', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=3, verbose_name='포트폴리오 평점')),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio', verbose_name='포트폴리오')),
            ],
            options={
                'verbose_name': 'Portfolio Comment',
                'verbose_name_plural': 'Portfolio Comments',
                'db_table': 'portfolio comment',
            },
        ),
    ]
