from django.contrib import admin
from import_export import resources

# Register your models here.
from import_export.admin import ImportMixin, ImportExportModelAdmin

from workallocation.forms import WorkloadForm
from workallocation.models import Workload, CaseStage


class WorkloadResource(resources.ModelResource):
    class Meta:
        model = Workload
        skip_unchanged = True
        import_id_fields = ['case_number']


class WorkloadAdmin(ImportExportModelAdmin):
    list_display = (
        'case_number',
        'business_group',
        'case_code',
        'ref_no',
        'pms_scheme',
        'date_case_received',
        'surname',
        'case_stage',
        'category',
        'sla_expiry_date',
        'allocated_user'
    )
    form = WorkloadForm
    resource_class = WorkloadResource

    def save_model(self, request, obj, form, change):
        old = Workload.objects.filter(pk=obj.pk).first()
        if old.case_stage != obj.case_stage:
            CaseStage.objects.create(
                workload=obj,
                user=request.user,
                case_stage=obj.case_stage
            )
        super().save_model(request, obj, form, change)


admin.site.site_header = 'Work Allocation Tool'

admin.site.register(Workload, WorkloadAdmin)
