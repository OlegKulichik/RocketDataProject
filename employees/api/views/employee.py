from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from employees.api.views.permission.group import GroupEmployeePermissions
from employees.api.serializers.employee import EmployeeSerializer

from employees.models import Employee


class EmployeeView(
    mixins.ListModelMixin,
    GenericViewSet,
):
    filterset_fields = ('level', )
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (GroupEmployeePermissions,)

    def get_queryset(self):
        try:
            employee = Employee.objects.filter(user=self.request.user)
            return employee
        except Employee.DoesNotExist:
            raise FileNotFoundError('Employee not found')
