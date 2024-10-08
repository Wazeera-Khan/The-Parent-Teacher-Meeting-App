# Generated by Django 5.0.6 on 2024-07-13 16:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptmapp', '0012_alter_cie_cie1_alter_cie_cie2_alter_cie_cie3'),
    ]

    operations = [
        migrations.CreateModel(
            name='GPA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField()),
                ('gpa', models.FloatField(blank=True, null=True)),
                ('student_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ptmapp.studentdetail')),
            ],
        ),
    ]
