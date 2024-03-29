# Generated by Django 3.2.9 on 2022-03-30 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_merge_0014_auto_20220317_1436_0022_auto_20220323_0120'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiltyard',
            options={'verbose_name': 'Ристалище', 'verbose_name_plural': 'Ристалище'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['last_name'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='club',
            name='rating',
            field=models.FloatField(default=0, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='user',
            name='club',
            field=models.ForeignKey(blank=True, default=0, on_delete=django.db.models.deletion.PROTECT, to='main.club', verbose_name='Клуб'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Боец'), (2, 'Глава клуба'), (3, 'Cекретарь')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='tiltyard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.tiltyard'),
        ),
    ]
