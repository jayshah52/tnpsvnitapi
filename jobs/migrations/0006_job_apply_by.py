# Generated by Django 3.1.11 on 2021-06-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_auto_20210605_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='apply_by',
            field=models.DateField(max_length=8, null=True),
        ),
    ]