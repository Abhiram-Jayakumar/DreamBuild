# Generated by Django 4.0.2 on 2022-03-29 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_rename_user_constructorbooking_user1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newworkerbooking',
            old_name='User',
            new_name='User2',
        ),
    ]
