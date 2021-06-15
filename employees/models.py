import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from core.enums.level import LevelEmployee
from core.enums.position import PositionStatus


class User(AbstractUser):
    middle_name = models.CharField(blank=True, null=True, max_length=255, default=None)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    position = models.CharField(max_length=12, choices=PositionStatus.items(), default=PositionStatus.BILLABLE.value)
    employee_start_date = models.DateTimeField(auto_now_add=True)
    amount_wages = models.PositiveIntegerField(default=500)
    total_amount_wages = models.PositiveIntegerField(blank=True, null=True)
    level = models.CharField(max_length=12, choices=LevelEmployee.items(), default=LevelEmployee.ONE.value)
    head = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, db_index=True)

    # @property
    # def total_amount_wages(self):
    #     if self.amount_wages:
    #         return (self.amount_wages / 30) * (datetime.datetime.now() - self.employee_start_date.utcnow()).days

    def __str__(self):
        return f'{self.user}'