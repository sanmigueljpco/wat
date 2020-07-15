from django.contrib import admin
from django.shortcuts import render
from django.contrib import messages
from import_export import resources

# Register your models here.
from import_export.admin import ImportMixin, ImportExportModelAdmin

from workallocation.forms import WorkloadForm, BulkAllocationForm
from workallocation.models import Workload, CaseStage


class WorkloadResource(resources.ModelResource):
    class Meta:
        model = Workload
        skip_unchanged = True
        import_id_fields = ['case_number']


class WorkloadAdmin(ImportExportModelAdmin):
    actions = ['bulk_allocation']
    action_form = BulkAllocationForm

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

    def bulk_allocation(self, request, queryset):
        user = int(request.POST['user'])
        queryset.update(allocated_user=user)
        messages.success(request, '{0} cases were assigned'.format(queryset.count()))

    bulk_allocation.short_description = 'Allocate'


admin.site.site_header = 'Work Allocation Tool'

admin.site.register(Workload, WorkloadAdmin)
