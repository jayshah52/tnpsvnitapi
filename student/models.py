from datetime import datetime

from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.
from django.forms import CharField


class Student(AbstractUser):
    GENDER = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
    CATEGORY = (
        ('GENERAL', 'General'),
        ('SC', 'SC'),
        ('ST', 'ST'),
        ('OBC', 'OBC'),
        ('OTHERS', 'OTHERS'),
    )
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    email = models.EmailField(unique=True)
    personal_mail = models.EmailField(null=True, blank=True)
    phone_no = models.CharField(max_length=10, null=True, blank=True, default='')
    roll_no = models.CharField(max_length=8,null=True, blank=True, default='')
    gender = models.CharField(max_length=6,choices=GENDER, default='MALE')
    dob = models.DateField(max_length=8, null=True)
    department = models.CharField(max_length=2, default='', null=True)
    category = models.CharField(max_length=7,choices=CATEGORY, default='GENERAL')
    hometown = models.CharField(max_length=255, null=True, blank=True, default='')
    percentage_ten = models.FloatField(null=True, blank=True, default=0)
    percentage_twelve = models.FloatField(null=True, blank=True, default=0)
    cur_backlog = models.IntegerField(null=True, blank=True, default=0)
    total_backlogs = models.IntegerField(null=True, blank=True, default=0)
    current_loc = models.CharField(max_length=255, null=True, blank=True, default='')
    cgpa_s1 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s2 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s3 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s4 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s5 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s6 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s7 = models.FloatField(null=True, blank=True, default=0)
    cgpa_s8 = models.FloatField(null=True, blank=True, default=0)
    is_coordinator = models.BooleanField(default=False)
    graduation_year = models.CharField(max_length=4, null=True, blank=True, default='')
    resume_link = models.URLField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.roll_no:
            self.roll_no = self.username
        if not self.department:
            self.department = self.roll_no[3:5].upper()
        super().save(*args, **kwargs)
