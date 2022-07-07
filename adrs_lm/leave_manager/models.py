from random import choices
from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.


# class LeaveType(models.Model):
# type = models.CharField(max_length=255, default='Annual Leave')

# def __str__(self):
# return self.type
class LeaveType(models.TextChoices):
    ANNNUAL = ("annual", "Annual Leave")
    SICK = ("sick", "Sick Leave")
    FAMILY_RESPONSIBILITY = ("family responsibility",
                             "Family Responsibility Leave")
    STUDY = ("study", "Study Leave")
    MATERNITY = ("maternity", "Maternity Leave")
    UNPAID = ("unpaid", "Unpaid Leave")


class Department(models.TextChoices):
    CALLCENTER = ("call center", "Call Center")
    ADMIN = ("admin", "Admin")
    PRELAEGAL = ("prelegal", "Prelegal")
    IT = ("it", "IT")
    HEAD_OFFICE = ("headoffice", "Head Office")
    HR = ("hr", "HR")
    FINANCE = ("finace", "Finance")
    MARKETING = ("marketing", "Marketing")


class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(
        "Leave Type", choices=LeaveType.choices, max_length=30, default=LeaveType.ANNNUAL, blank=True, null=True)
    from_date = models.DateField(default=datetime.date.today)
    to_date = models.DateField(default=datetime.date.today)
    reason = models.TextField(max_length=1200, default='Not Feeling Well')
    department = models.CharField("Department", choices=Department.choices,
                                  max_length=60, default=Department.CALLCENTER, blank=True, null=True)
    leave_balance = models.CharField(max_length=2, blank=True, null=True)
    number_of_days_taken = models.IntegerField(blank=True, null=True)
    days_paid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.leave_type
