# Generated by Django 3.2.9 on 2022-03-22 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220322_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='tiltyard',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='main.tiltyard'),
        ),
    ]
