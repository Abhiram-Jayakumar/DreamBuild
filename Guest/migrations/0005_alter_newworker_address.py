# Generated by Django 4.0.2 on 2022-03-03 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_alter_newconstructor_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newworker',
            name='Address',
            field=models.TextField(max_length=50),
        ),
    ]
