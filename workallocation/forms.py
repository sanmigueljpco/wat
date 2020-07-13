from django import forms
from django.contrib.auth.models import User

from workallocation.models import Workload

STAGES = (
    ('Doing', 'Doing'),
    ('Checking', 'Checking'),
    ('Complete', 'Complete'),
)


class WorkloadForm(forms.ModelForm):
    allocated_user = forms.ModelChoiceField(queryset=User.objects.all())

    class Meta:
        model = Workload
        fields = [
            'business_group',
            'case_code',
            'ref_no',
            'pms_scheme',
            'date_case_received',
            'surname',
            'case_stage',
            'category',
            'sla_expiry_date'
        ]
        widgets = {
            'business_group': forms.TextInput(attrs={'readonly': 'readonly'}),
            'case_code': forms.TextInput(attrs={'readonly': 'readonly'}),
            'ref_no': forms.TextInput(attrs={'readonly': 'readonly'}),
            'pms_scheme': forms.TextInput(attrs={'readonly': 'readonly'}),
            'date_case_received': forms.TextInput(attrs={'readonly': 'readonly'}),
            'surname': forms.TextInput(attrs={'readonly': 'readonly'}),
            'case_stage': forms.Select(choices=STAGES),
            'category': forms.TextInput(attrs={'readonly': 'readonly'}),
            'sla_expiry_date': forms.TextInput(attrs={'readonly': 'readonly'})
        }
