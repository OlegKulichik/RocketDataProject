from django.utils.html import format_html
from django.contrib import admin

from employees.models import Employee, User

from RocketDataProject.tasks import remove_total_amount_wages


@admin.action(description='Mark employee to reset the total amount wages')
def nullify_total_amount_wages(modeladmin, request, queryset):
    if len(queryset) >= 20:
        remove_total_amount_wages.delay(list(queryset.all().values_list('id', flat=True)))
    else:
        queryset.update(total_amount_wages=0)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'head_link', 'amount_wages', 'total_amount_wages')
    list_filter = ('position', 'level',)
    actions = (nullify_total_amount_wages,)
    readonly_fields = ('employee_start_date',)

    @staticmethod
    def head_link(obj):
        if obj.head:
            return format_html('<a href="/admin/employees/employee/{}"> {} </a>', obj.head.id, obj.head)
        return format_html('<a href="/admin/employees/employee/{}"> Head not appointed </a>', obj.id)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(User)
