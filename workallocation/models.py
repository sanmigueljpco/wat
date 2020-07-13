from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Workload(models.Model):
    range = models.IntegerField(blank=True, null=True)
    business_group = models.CharField(max_length=120)
    case_code = models.CharField(max_length=15)
    case_number = models.IntegerField()
    ref_no = models.CharField(max_length=30)
    pension_scheme = models.CharField(max_length=30)
    pms_scheme = models.CharField(max_length=10)
    case_group = models.CharField(max_length=30)
    date_case_received = models.DateField()
    initials = models.CharField(max_length=5)
    surname = models.CharField(max_length=30)
    allocated_user = models.CharField(max_length=50)
    case_notes = models.CharField(blank=True, null=True, max_length=500)
    case_stage = models.CharField(max_length=20)
    category = models.CharField(blank=True, null=True, max_length=10)
    allocated_team = models.CharField(max_length=30)
    date_case_started = models.DateField(blank=True, null=True)
    no_of_units = models.IntegerField()
    sla_clock_stopped = models.CharField(max_length=10)
    owner_team = models.CharField(max_length=20)
    owner_region = models.CharField(max_length=20)
    allocated_region = models.CharField(max_length=30)
    sla_expiry_date = models.DateField()
    next_reminder_due_date = models.DateField(blank=True, null=True)
    workload_planning_date = models.DateField()


class CaseStage(models.Model):
    id = models.IntegerField(primary_key=True)
    workload = models.ForeignKey(Workload, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    case_stage = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
