from rest_framework.permissions import BasePermission
from django.contrib.auth.models import Group


class GroupEmployeePermissions(BasePermission):

    ALLOWED_GROUP = 'PermissionGroup'

    def has_permission(self, request, view):
        return True if self.ALLOWED_GROUP in list(request.user.groups.all().values_list('name', flat=True)) else False
