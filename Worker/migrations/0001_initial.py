# Generated by Django 4.0.2 on 2022-03-05 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workerprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rate', models.CharField(max_length=20)),
                ('Discription', models.CharField(max_length=50)),
                ('Experience', models.CharField(max_length=50)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.workcategory')),
            ],
        ),
    ]
