from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
import jwt
from datetime import datetime, timedelta


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
    club = models.ForeignKey('Club', on_delete=models.PROTECT, blank=True, null=True, verbose_name='Клуб')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    is_staff = models.BooleanField(default=False, verbose_name='Доступ к сайту администратора')
    is_active = models.BooleanField(default=False, verbose_name='Активность учётной записи')

    # -------------------------------------------------------------------------------------
    number = models.IntegerField(default=0, blank=True, verbose_name='Номер бойца')
    
    victoryPoints = models.IntegerField(default=0, blank=True, verbose_name='Количество побед')
    pool = models.IntegerField(default=0, blank=True, verbose_name='Пул')
    tiltyard = models.ForeignKey('Tiltyard', on_delete=models.CASCADE, related_name='+', null=True, blank=True, verbose_name='Ристалище')
    stage = models.IntegerField(default=0, blank=True, verbose_name='Стадия')

    YOUNG_FIGHTER = 0
    THIRD_YOUNG = 1
    SECOND_YOUNG = 2
    FIRST_YOUNG = 3
    THIRD_ADULT = 4
    SECOND_ADULT = 5
    FIRST_ADULT = 6
    KMS = 7
    MC = 8
    MCMK = 9
    # ZMC = 10
    
    CATEGORY_CHOICES = (
        (YOUNG_FIGHTER, 'Юный боец'),
        (THIRD_YOUNG, '3 Юнешеский'),
        (SECOND_YOUNG, '2 Юнешеский'),
        (FIRST_YOUNG, '1 Юнешеский'),
        (THIRD_ADULT, '3 Взрослый'),
        (SECOND_ADULT, '2 Взрослый'),
        (FIRST_ADULT, '1 Взрослый'),
        (KMS, 'КМС'),
        (MC, 'МС'),
        (MCMK, 'МСМК'),
        # (ZMC, 'ЗМС'),
    )

    category = models.IntegerField(choices=CATEGORY_CHOICES, blank=False, null=False, default=0, verbose_name='Категория')

    FIGHTER = 1
    DM = 2
    SECRETARITY = 3
    REFEREE = 4
    
    ROLE_CHOICES = (
        (FIGHTER, 'Боец'),
        (DM, 'Глава клуба'),
        (SECRETARITY, 'Cекретарь'),
        (REFEREE, 'Судья'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=1, verbose_name='Роль')
    # -------------------------------------------------------------------------------------

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['last_name']

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
    rating = models.FloatField(default=0, verbose_name='Рейтинг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клуб'
        verbose_name_plural = 'Клубы'
        ordering = ['-rating']


class Tiltyard(models.Model):

    PREPARATION = "Подготовка"
    GOES = "Идет"
    FINISHED = "Оконченно"
    
    STATE_CHOICES = (
        (PREPARATION, 'Подготовка'),
        (GOES, 'Идет'),
        (FINISHED, 'Оконченно'),
    )

    name = models.CharField(max_length=50)
    nomination = models.CharField(max_length=50,  null=True, blank=True,)
    age_category = models.CharField(max_length=50,  null=True, blank=True,)
    league = models.CharField(max_length=50,  null=True, blank=True,)
    state = models.CharField(choices=STATE_CHOICES, default=1, max_length=10,  null=True, blank=True,)
    referee = models.OneToOneField("User", on_delete=models.CASCADE, related_name='+',  null=True, blank=True,)
    stage = models.IntegerField(default=1,  null=True, blank=True, verbose_name="Этап")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ристалище'
        verbose_name_plural = 'Ристалище'


class BattleOrder(models.Model):
    left_fighter =  models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Левый боец',  related_name='Left')
    right_fighter =  models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Правый боец',  related_name='Right')
    Tiltyard =  models.ForeignKey('Tiltyard', on_delete=models.PROTECT, verbose_name='Ристалище')
    Order = models.PositiveSmallIntegerField(verbose_name="Порядок")
    stage = models.IntegerField(default=1,  null=True, blank=True, verbose_name="Этап")
    left_scores = models.IntegerField(default=0, blank=True, verbose_name='Очки за бой левого бойца')
    right_scores = models.IntegerField(default=0, blank=True, verbose_name='Очки за бой правого бойца')

    def __str__(self):
        return self.Tiltyard

    class Meta:
        verbose_name = 'Порядок боев'
        verbose_name_plural = 'Порядки боев'
        ordering = ['-Tiltyard']
