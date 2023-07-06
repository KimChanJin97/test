# Generated by Django 4.2.2 on 2023-07-06 05:34

from django.db import migrations, models
import multiselectfield.db.fields
import user.models.user
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='유저 고유번호')),
                ('kakaoId', models.IntegerField(default=1, null=True, verbose_name='카카오 id')),
                ('kakao_thumbnail_url', models.URLField(null=True, verbose_name='카카오 유저 썸네일 url')),
                ('thumbnail_image', models.ImageField(null=True, upload_to='', verbose_name='일반 유저 썸네일 이미지')),
                ('email', models.CharField(max_length=255, null=True, unique=True, verbose_name='카카오 이메일')),
                ('name', models.CharField(max_length=10, null=True, verbose_name='이름')),
                ('phone_number', models.CharField(max_length=20, null=True, unique=True, verbose_name='전화번호')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='생년월일')),
                ('field', multiselectfield.db.fields.MultiSelectField(choices=[(0, 'FRONTEND'), (1, 'HOMEPAGE'), (2, 'APPLICATION'), (3, 'GAME'), (4, 'BACKEND'), (5, 'DATA'), (6, 'WEB_MOBILE_DESIGN'), (7, 'VISUAL_DESIGN'), (8, 'LOGO_BRAND_DESIGN'), (9, 'PACKAGE_DESIGN'), (10, 'PRODUCT_DESIGN'), (11, 'CONSTRUCTION_DESIGN'), (12, 'INTERIOR_DESIGN'), (13, 'EXHIBITION_DESIGN'), (14, 'FASHION_DESIGN'), (15, 'JEWERLY_DESIGN'), (16, 'FABRIC_DESIGN'), (17, 'INDUSTRIAL_DESIGN'), (18, 'MEDIA_DESIGN'), (19, 'MOTION_GRAPHIC'), (20, 'FINE_ART')], max_length=21)),
                ('job', models.CharField(choices=[(0, 'student'), (1, 'teenager'), (2, 'employee'), (3, 'freelancer'), (4, 'start_up'), (5, 'job_seeker'), (6, 'etc')], default='student', max_length=10, null=True, verbose_name='직업')),
                ('univ', models.CharField(max_length=20, null=True, verbose_name='대학교')),
                ('major', models.CharField(max_length=20, null=True, verbose_name='전공')),
                ('univ_identification', models.ImageField(upload_to=user.models.user.image_upload_path, verbose_name='대학 증명서')),
                ('univ_email', models.CharField(max_length=40, null=True, verbose_name='대학 이메일')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
            },
        ),
    ]
