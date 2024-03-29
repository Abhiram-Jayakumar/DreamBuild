# Generated by Django 4.0.2 on 2022-05-03 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_admin'),
        ('Guest', '0012_remove_newconstructor_construct_bookingstatus'),
        ('Landlord', '0004_rename_district_managelands_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='landlordComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=200)),
                ('Complaint_Date', models.DateTimeField(auto_now=True)),
                ('Complaintreply', models.CharField(default='No reply', max_length=200)),
                ('Complaint_Status', models.IntegerField(default=False)),
                ('complaint_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Admin.complainttype')),
                ('landlord', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.newlandlord')),
            ],
        ),
    ]
