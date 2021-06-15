from django.contrib import admin
from django.utils.html import format_html

from employees.models import Employee, User


@admin.action(description='Mark employee to reset the total amount wages')
def nullify_total_amount_wages(modeladmin, request, queryset):
    queryset.update(total_amount_wages=None)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'head_link', 'amount_wages', 'total_amount_wages')
    list_filter = ('position', 'level',)
    actions = (nullify_total_amount_wages,)
    readonly_fields = ('employee_start_date',)

    @staticmethod
    def head_link(obj):
        return format_html('<a href="/admin/employees/employee/{}"> {} </a>', obj.head.id, obj.head)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(User)
