# Generated by Django 3.2.8 on 2023-11-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grades_app', '0002_alter_students_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='Start_year',
            field=models.IntegerField(),
        ),
    ]
