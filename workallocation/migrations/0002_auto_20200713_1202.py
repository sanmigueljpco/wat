# Generated by Django 3.0.8 on 2020-07-13 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workallocation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workload',
            name='case_notes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='workload',
            name='category',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='workload',
            name='date_case_started',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workload',
            name='next_reminder_due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workload',
            name='range',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='CaseStage',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('case_stage', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workallocation.Workload')),
            ],
        ),
    ]
