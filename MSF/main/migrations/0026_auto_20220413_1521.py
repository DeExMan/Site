# Generated by Django 3.2.9 on 2022-04-13 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_user_club'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, default=0, verbose_name='Номер бойца'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pool',
            field=models.IntegerField(blank=True, default=0, verbose_name='Пул'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Боец'), (2, 'Глава клуба'), (3, 'Cекретарь'), (4, 'Судья')], default=1, null=True, verbose_name='Роль'),
        ),
        migrations.AlterField(
            model_name='user',
            name='scores',
            field=models.IntegerField(blank=True, default=0, verbose_name='Очки за бой'),
        ),
        migrations.AlterField(
            model_name='user',
            name='stage',
            field=models.IntegerField(blank=True, default=0, verbose_name='Стадия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='tiltyard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.tiltyard', verbose_name='Ристалище'),
        ),
        migrations.AlterField(
            model_name='user',
            name='victoryPoints',
            field=models.IntegerField(blank=True, default=0, verbose_name='Количество побед'),
        ),
        migrations.CreateModel(
            name='BattleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tiltyard', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.tiltyard', verbose_name='Ристалище')),
                ('left_fighter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Left', to=settings.AUTH_USER_MODEL, verbose_name='Левый боец')),
                ('right_fighter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Right', to=settings.AUTH_USER_MODEL, verbose_name='Правый боец')),
            ],
            options={
                'verbose_name': 'Порядок боев',
                'verbose_name_plural': 'Порядки боев',
                'ordering': ['-Tiltyard'],
            },
        ),
    ]
