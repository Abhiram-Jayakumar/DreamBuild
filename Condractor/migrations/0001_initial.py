# Generated by Django 4.0.2 on 2022-03-05 05:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0006_alter_newconstructor_proof1_and_more'),
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='previouswork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Squarefeet', models.CharField(max_length=20)),
                ('Photo', models.FileField(upload_to='Previousworkimage/')),
                ('Description', models.CharField(max_length=70)),
                ('Totalamount', models.CharField(max_length=20)),
                ('Duration', models.CharField(max_length=20)),
                ('Condractor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.newconstructor')),
                ('Type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.contractservice')),
            ],
        ),
    ]
