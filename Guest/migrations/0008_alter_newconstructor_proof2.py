# Generated by Django 4.0.2 on 2022-03-07 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0007_alter_newconstructor_proof1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newconstructor',
            name='Proof2',
            field=models.FileField(upload_to='identyproof2/'),
        ),
    ]
