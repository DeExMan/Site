# Generated by Django 3.2.9 on 2022-05-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20220422_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Юный боец'), (1, '3 Юнешеский'), (2, '2 Юнешеский'), (3, '1 Юнешеский'), (4, '3 Взрослый'), (5, '2 Взрослый'), (6, '1 Взрослый'), (7, 'КМС'), (8, 'МС'), (9, 'МСМК'), (10, 'ЗМС')], default=0, verbose_name='Роль'),
        ),
    ]
