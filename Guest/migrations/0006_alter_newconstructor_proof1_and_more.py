# Generated by Django 4.0.2 on 2022-03-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0005_alter_newworker_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newconstructor',
            name='Proof1',
            field=models.FileField(upload_to='identityproof1/'),
        ),
        migrations.AlterField(
            model_name='newconstructor',
            name='Proof2',
            field=models.FileField(upload_to='identityproof2/'),
        ),
    ]