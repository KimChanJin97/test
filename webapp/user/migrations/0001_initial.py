# Generated by Django 4.2.2 on 2023-06-30 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import user.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('kakaoId', models.IntegerField(default=1, null=True, verbose_name='카카오 id')),
                ('thumbnail_image', models.URLField(null=True, verbose_name='카카오 썸네일 이미지')),
                ('email', models.CharField(max_length=255, null=True, unique=True, verbose_name='카카오 이메일')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='이름')),
                ('phone_number', models.CharField(max_length=20, null=True, unique=True, verbose_name='전화번호')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='생년월일')),
                ('job', models.CharField(choices=[(0, 'student'), (1, 'teenager'), (2, 'employee'), (3, 'freelancer'), (4, 'start_up'), (5, 'job_seeker'), (6, 'etc')], default='student', max_length=10, null=True, verbose_name='직업')),
                ('univ', models.CharField(max_length=20, null=True, verbose_name='대학교')),
                ('major', models.CharField(max_length=20, null=True, verbose_name='전공')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='UserUnivIdentification',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('univ_identification', models.ImageField(upload_to=user.models.user.image_upload_path)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='univ_identification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
