# Generated by Django 3.2.9 on 2022-03-22 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Боец'), (2, 'Глава клуба'), (3, 'Cекретарь')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tiltyard',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.tiltyard'),
        ),
    ]