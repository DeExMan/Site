# Generated by Django 3.2.9 on 2022-03-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_user_tiltyard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiltyard',
            name='state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Подготовка'), (2, 'Идет'), (3, 'Оконченно')], default=1),
        ),
    ]