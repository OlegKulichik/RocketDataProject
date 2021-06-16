from celery import shared_task
from employees.models import Employee
from django.db.models import F


@shared_task
def accrual_wages():
    Employee.objects.update(total_amount_wages=F('total_amount_wages')+F('amount_wages'))


@shared_task()
def remove_total_amount_wages(queryset):
    queryset.update(total_amount_wages=0)

