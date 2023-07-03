# Generated by Django 4.2.2 on 2023-07-03 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('work', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='adder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='유저'),
        ),
        migrations.AddField(
            model_name='bookmark',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='work.work', verbose_name='북마크 작업물'),
        ),
    ]