# Generated by Django 3.0.8 on 2020-07-11 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.IntegerField()),
                ('business_group', models.CharField(max_length=120)),
                ('case_code', models.CharField(max_length=15)),
                ('case_number', models.IntegerField()),
                ('ref_no', models.CharField(max_length=30)),
                ('pension_scheme', models.CharField(max_length=30)),
                ('pms_scheme', models.CharField(max_length=10)),
                ('case_group', models.CharField(max_length=30)),
                ('date_case_received', models.DateField()),
                ('initials', models.CharField(max_length=5)),
                ('surname', models.CharField(max_length=30)),
                ('allocated_user', models.CharField(max_length=50)),
                ('case_notes', models.CharField(max_length=500)),
                ('case_stage', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=10)),
                ('allocated_team', models.CharField(max_length=30)),
                ('date_case_started', models.DateField()),
                ('no_of_units', models.IntegerField()),
                ('sla_clock_stopped', models.CharField(max_length=10)),
                ('owner_team', models.CharField(max_length=20)),
                ('owner_region', models.CharField(max_length=20)),
                ('allocated_region', models.CharField(max_length=30)),
                ('sla_expiry_date', models.DateField()),
                ('next_reminder_due_date', models.DateField()),
                ('workload_planning_date', models.DateField()),
            ],
        ),
    ]
