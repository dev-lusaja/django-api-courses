# Generated by Django 4.1.7 on 2023-03-31 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
        migrations.RenameModel(
            old_name='Enrollments',
            new_name='Enrollment',
        ),
        migrations.RenameModel(
            old_name='Students',
            new_name='Parent',
        ),
        migrations.RenameModel(
            old_name='Parents',
            new_name='Student',
        ),
    ]
