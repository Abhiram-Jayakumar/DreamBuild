# Generated by Django 4.0.2 on 2022-04-09 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0010_newlandlord_newlandlor_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='newconstructor',
            name='construct_bookingstatus',
            field=models.IntegerField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='newworker',
            name='worker_bookingstatus',
            field=models.IntegerField(default=False, null=True),
        ),
    ]
