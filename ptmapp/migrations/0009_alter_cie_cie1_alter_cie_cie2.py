# Generated by Django 5.0.6 on 2024-07-13 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptmapp', '0008_remove_cie_cie3_alter_cie_cie1_alter_cie_cie2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cie',
            name='cie1',
            field=models.FloatField(blank=True, default='N/A', null=True),
        ),
        migrations.AlterField(
            model_name='cie',
            name='cie2',
            field=models.FloatField(blank=True, default='N/A', null=True),
        ),
    ]
