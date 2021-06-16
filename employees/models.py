from django.contrib.auth.models import AbstractUser
from django.db import models

from core.enums.position import PositionStatus
from core.enums.level import LevelEmployee


class User(AbstractUser):
    middle_name = models.CharField(blank=True, null=True, max_length=255, default=None)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    position = models.CharField(max_length=12, choices=PositionStatus.items(), default=PositionStatus.POS5.value)
    employee_start_date = models.DateTimeField(auto_now_add=True)
    amount_wages = models.PositiveIntegerField(default=500)
    total_amount_wages = models.PositiveIntegerField(default=0)
    level = models.CharField(max_length=12, choices=LevelEmployee.items(), default=LevelEmployee.ONE.value)
    head = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)

    def __str__(self):
        return f'{self.user}'
