# Generated by Django 3.2.9 on 2022-03-16 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20220316_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiltyard',
            name='referee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.user'),
        ),
    ]
