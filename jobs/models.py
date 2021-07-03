from django.db import models

# Create your models here.
from student.models import Student
from multiselectfield import MultiSelectField


class Job(models.Model):
    DEPARTMENTS = (
        ('CO', 'Computer Engineering'),
        ('EC', 'Electronics & Communication Engineering'),
        ('EE', 'Electrical Engineering'),
        ('CE', 'Civil Engineering'),
        ('CH', 'Chemical Engineering'),
        ('ME', 'Mechanical Engineering'),
    )
    TYPES = (
        ('INTERNSHIP', 'Internship'),
        ('PLACEMENT', 'Placement')
         )
    users = models.ManyToManyField(Student)
    role = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    company_desc = models.TextField(null=True, blank=True)
    job_desc = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(Student, related_name='student', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now=True)
    ctc = models.CharField(max_length=254, null=True, blank=True)
    grad_year = models.CharField(max_length=254, null=True, blank=True)
    for_departments = MultiSelectField(choices=DEPARTMENTS)
    job_type = models.CharField(max_length=12,choices=TYPES, default='PLACEMENT')
    status = models.BooleanField(default=True)
    criteria = models.TextField()
    apply_by = models.DateField(max_length=8, null=True)
    jd = models.FileField(upload_to='jd/pdf', null=True)

    def __str__(self):
        return str(self.role)

class Shortlist(models.Model):

    NUMBER = (
        (1, 'First'),
        (2, 'Second'),
        (3, 'Third'),
        (4, 'Final')
    )
    job  = models.ForeignKey(Job, related_name='job', on_delete=models.CASCADE)
    users = models.ManyToManyField(Student)
    created_at = models.DateTimeField(auto_now=True)
    number = models.IntegerField(choices=NUMBER, default=1)
    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return str(self.job.name) + str(self.number) + ' Shortlist'
