# Generated by Django 5.0.6 on 2024-07-14 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ptmapp', '0015_alter_notification_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='attendees',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='AttendanceResponse',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
