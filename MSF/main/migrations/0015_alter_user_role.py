# Generated by Django 3.2.9 on 2022-03-17 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20220317_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.IntegerField(blank=True, choices=[(1, 'Боец'), (2, 'Глава клуба'), (3, 'Cекретарь')], default=1, null=True),
        ),
    ]