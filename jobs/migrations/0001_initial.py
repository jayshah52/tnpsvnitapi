# Generated by Django 3.1.11 on 2021-05-30 19:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True)),
                ('company_desc', models.TextField(blank=True, null=True)),
                ('job_desc', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('ctc', models.CharField(blank=True, max_length=254, null=True)),
                ('grad_year', models.CharField(blank=True, max_length=254, null=True)),
                ('for_departments', multiselectfield.db.fields.MultiSelectField(choices=[('CO', 'Computer Engineering'), ('EC', 'Electronics & Communication Engineering'), ('EE', 'Electrical Engineering'), ('CE', 'Civil Engineering'), ('CH', 'Chemical Engineering'), ('ME', 'Mechanical Engineering')], max_length=17)),
                ('job_type', models.IntegerField(choices=[('INTERNSHIP', 'Internship'), ('PLACEMENT', 'Placement')], default='PLACEMENT')),
                ('status', models.BooleanField(default=True)),
                ('criteria', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]