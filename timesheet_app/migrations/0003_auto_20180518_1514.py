# Generated by Django 2.0.5 on 2018-05-18 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesheet_app', '0002_auto_20180518_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeform',
            name='total_week_hours',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
