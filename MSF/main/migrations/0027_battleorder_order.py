# Generated by Django 3.2.9 on 2022-04-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20220413_1521'),
    ]

    operations = [
        migrations.AddField(
            model_name='battleorder',
            name='Order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Порядок'),
            preserve_default=False,
        ),
    ]