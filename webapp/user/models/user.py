from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from multiselectfield import MultiSelectField
import uuid

STUDENT = 0
TEENAGER = 1
EMPLOYEE = 2
FREELANCER = 3
START_UP = 4
JOB_SEEKER = 5
ETC = 6

JOB_CHOICES = ((STUDENT, 'student'),
               (TEENAGER, 'teenager'),
               (EMPLOYEE, 'employee'),
               (FREELANCER, 'freelancer'),
               (START_UP, 'start_up'),
               (JOB_SEEKER, 'job_seeker'),
               (ETC, 'etc'))

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


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()

    def create_user(self, email, password, **kwargs):
        """일반 유저 생성 메소드"""
        self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        """슈퍼 유저(superuser) 생성 메소드"""
        kwargs.setdefault('is_superuser', True)
        self._create_user(email, password, **kwargs)


def image_upload_path(instance, filename):
    return f'{instance.email}/{filename}'


class User(AbstractBaseUser, PermissionsMixin):
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    user_uuid = models.UUIDField(
        verbose_name="유저 고유번호",
        primary_key=True,
        null=False,
        default=uuid.uuid4
    )
    kakaoId = models.IntegerField(
        verbose_name="카카오 id",
        null=True,
        default=1,
    )
    kakao_thumbnail_url = models.URLField(
        verbose_name="카카오 유저 썸네일 url",
        null=True,
    )
    thumbnail_image = models.ImageField(
        verbose_name="일반 유저 썸네일 이미지"
    )
    email = models.CharField(
        verbose_name="카카오 이메일",
        max_length=255,
        null=True,
        unique=True,
    )
    name = models.CharField(
        verbose_name='이름',
        max_length=10,
        null=True,
    )
    phone_number = models.CharField(
        verbose_name='전화번호',
        max_length=20,
        null=True,
        unique=True,
    )
    birth_date = models.DateField(
        verbose_name='생년월일',
        null=True,
        blank=True,
    )
    field = MultiSelectField(
        choices=INTERESTS,
        max_length=len(INTERESTS),
    )
    job = models.CharField(
        verbose_name='직업',
        choices=JOB_CHOICES,
        max_length=10,
        default="student",
        null=True,
    )
    univ = models.CharField(
        verbose_name='대학교',
        max_length=20,
        null=True,
    )
    major = models.CharField(
        verbose_name='전공',
        max_length=20,
        null=True,
    )
    univ_identification = models.ImageField(
        verbose_name='대학 증명서',
        upload_to=image_upload_path,
    )
    univ_email = models.CharField(
        verbose_name='대학 이메일',
        max_length=40,
        null=True,
    )


    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self) -> str:
        simplified_email = str(self.email).split('@')[0]
        return f'{self.name}({simplified_email})'
