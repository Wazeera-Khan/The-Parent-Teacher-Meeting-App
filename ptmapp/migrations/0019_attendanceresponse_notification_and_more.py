# Generated by Django 5.0.6 on 2024-07-14 12:10

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptmapp', '0018_remove_notification_attendees_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceResponse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.BooleanField(default=None, null=True)),
                ('student_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptmapp.studentdetail')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('meeting_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('attendees', models.ManyToManyField(through='ptmapp.AttendanceResponse', to='ptmapp.studentdetail')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='ptmapp.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='attendanceresponse',
            name='notification',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptmapp.notification'),
        ),
    ]
