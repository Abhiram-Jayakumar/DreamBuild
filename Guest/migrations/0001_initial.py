# Generated by Django 4.0.2 on 2022-02-26 05:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Contact', models.CharField(max_length=30)),
                ('Gender', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254, unique=True)),
                ('Address', models.TextField(unique=True)),
                ('Password', models.CharField(max_length=20, unique=True)),
                ('Place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.place')),
            ],
        ),
    ]
