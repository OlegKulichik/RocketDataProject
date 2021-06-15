from rest_framework import serializers

from employees.models import Employee, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
        )


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Employee
        fields = (
            'user',
            'position',
            'total_amount_wages',
            'employee_start_date',
            'amount_wages',
            'level',
            'head',
        )
