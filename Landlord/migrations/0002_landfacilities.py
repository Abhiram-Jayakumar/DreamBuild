# Generated by Django 4.0.2 on 2022-03-12 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0001_initial'),
        ('Landlord', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Landfacilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Discription', models.CharField(max_length=50)),
                ('Photo', models.FileField(upload_to='Landfacilities/')),
                ('Facilities', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.landfactors')),
                ('Land', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Landlord.managelands')),
            ],
        ),
    ]