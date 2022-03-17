from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='Адрес электронной почты')
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=30, blank=True, verbose_name='Отчество')
    club = models.ForeignKey('Club', on_delete=models.PROTECT, null=True, verbose_name='Клуб')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    is_staff = models.BooleanField(default=False, verbose_name='Доступ к сайту администратора')
    is_active = models.BooleanField(default=False, verbose_name='Активность учётной записи')

    number = models.IntegerField(default=0)
    scores = models.IntegerField(default=0)
    victoryPoints = models.IntegerField(default=0)
    pool = models.IntegerField(default=0)
    tiltyard = models.ForeignKey('Tiltyard', on_delete=models.CASCADE, related_name='+', null=True)
    stage = models.IntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email

    def get_full_name(self):
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.patronymic)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Club(models.Model):
    name = models.CharField(max_length=80, db_index=True, verbose_name='Название клуба')
    fighters_counter = models.IntegerField(default=0, verbose_name='Количество бойцов')
    rating = models.FloatField(verbose_name='Рейтинг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'
        ordering = ['-rating']


class Tiltyard(models.Model):
    name = models.CharField(max_length=50)
    nomination = models.CharField(max_length=50)
    age_category = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    state = models.CharField(max_length=10)
    referee = models.OneToOneField("User", on_delete=models.CASCADE, related_name='+',)
    stage = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ристалище'
        verbose_name_plural = 'Ристалище'
