# Generated by Django 3.2.5 on 2021-07-13 07:31

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0009_alter_job_jd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='for_departments',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('CO', 'Computer Engineering'), ('CS', 'Computer Science Engineering'), ('EC', 'Electronics & Communication Engineering'), ('EE', 'Electrical Engineering'), ('CE', 'Civil Engineering'), ('CH', 'Chemical Engineering'), ('ME', 'Mechanical Engineering')], max_length=20),
        ),
    ]