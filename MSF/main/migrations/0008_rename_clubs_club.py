# Generated by Django 3.2.9 on 2022-03-15 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_user_club'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clubs',
            new_name='Club',
        ),
    ]
