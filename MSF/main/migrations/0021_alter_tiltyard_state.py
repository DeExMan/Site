# Generated by Django 3.2.9 on 2022-03-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_tiltyard_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiltyard',
            name='state',
            field=models.CharField(choices=[('Подготовка', 'Подготовка'), ('Идет', 'Идет'), ('Оконченно', 'Оконченно')], default=1, max_length=50),
        ),
    ]