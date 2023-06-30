from datetime import date

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


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


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

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

    kakaoId = models.IntegerField(
        verbose_name="카카오 id",
        null=True,
        default=1,
    )

    thumbnail_image = models.URLField(
        verbose_name="카카오 썸네일 이미지",
        null=True,
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

    objects = UserManager()

    USERNAME_FIELD = 'email'

    @property
    def is_staff(self):
        return self.is_superuser

    def __str__(self) -> str:
        return f'{self.email}'


def image_upload_path(instance, filename):
    return f'{instance.user.email}/{filename}'


class UserUnivIdentification(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='univ_identification')
    univ_identification = models.ImageField(upload_to=image_upload_path)
