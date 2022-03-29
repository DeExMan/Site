# Generated by Django 3.2.9 on 2022-03-17 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_tiltyard_referee'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiltyard',
            options={'verbose_name': 'Ристалище', 'verbose_name_plural': 'Ристалища'},
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Боец'), (2, 'Глава клуба'), (3, 'Секретарь')], default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='tiltyard',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='main.tiltyard'),
        ),
    ]
