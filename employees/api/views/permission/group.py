from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class GroupEmployeePermissions(BasePermission):

    def has_permission(self, request, view):
        names = []
        groups = Group.objects.filter(user=request.user.id).values_list('name')

        for groups_name in groups:
            names.append(*groups_name)
        if 'NameGroup' in names:
            return True
        return False
