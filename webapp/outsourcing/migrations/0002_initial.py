# Generated by Django 4.2.2 on 2023-07-07 03:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('outsourcing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outsourcingcomment',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='댓글 작성자'),
        ),
        migrations.AddField(
            model_name='outsourcing',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolio', verbose_name='포트폴리오'),
        ),
    ]
