from django.db import models
from datetime import datetime

# Create your models here.


class TimeForm(models.Model):
    LUNCH = (
        ('Yes', "Yes"),
        ('No', "No"),
    )

    employee = models.ForeignKey("auth.User", on_delete=models.CASCADE, related_name="timeform")
    time_sheet_week_from = models.DateField(blank=True, null=True)
    time_sheet_week_to = models.DateField(blank=True, null=True)
    total_week_hours = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)

    ## MONDAY: ##
    # Monday Date:
    date_mon = models.DateField(blank=True, null=True)
    # Time In:
    time_in_mon = models.TimeField(blank=True, null=True)
    # Time Out:
    time_out_mon = models.TimeField(blank=True, null=True)
    # If lunch == "Yes": -0.30 (or -30 min) to hours
    lunch_mon = models.CharField(max_length=4, choices=LUNCH, default="")
    # Vehicle:
    vehicles_mon = models.CharField(max_length=250, blank=True, null=True)
    # Job Addr + Desc:
    job_address_mon = models.CharField(max_length=250, blank=True, null=True)
    job_description_mon = models.CharField(max_length=250, blank=True, null=True)
    # Total hours Monday:
    C = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)


    ## TUE: ##
    # Date:
    date_tue = models.DateField(blank=True, null=True)
    # Time In:
    time_in_tue = models.TimeField(blank=True, null=True)
    # Time Out:
    time_out_tue = models.TimeField(blank=True, null=True)
    # If lunch == "Yes": -0.30 (or -30 min) to hours
    lunch_tue = models.CharField(max_length=4, choices=LUNCH, default="")
    # Vehicle:
    vehicles_tue = models.CharField(max_length=250, blank=True, null=True)
    # Job Addr + Desc:
    job_address_tue = models.CharField(max_length=250, blank=True, null=True)
    job_description_tue = models.CharField(max_length=250, blank=True, null=True)
    # Total hours Monday:
    hours_tue = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)


    ## WED: ##
    # Date:
    date_wed = models.DateField(blank=True, null=True)
    # Time In:
    time_in_wed = models.TimeField(blank=True, null=True)
    # Time Out:
    time_out_wed = models.TimeField(blank=True, null=True)
    # If lunch == "Yes": -0.30 (or -30 min) to hours
    lunch_wed = models.CharField(max_length=4, choices=LUNCH, default="")
    # Vehicle:
    vehicles_wed = models.CharField(max_length=250, blank=True, null=True)
    # Job Addr + Desc:
    job_address_wed = models.CharField(max_length=250, blank=True, null=True)
    job_description_wed = models.CharField(max_length=250, blank=True, null=True)
    # Total hours:
    hours_wed = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)


    ## THU: ##
    # Date:
    date_thu = models.DateField(blank=True, null=True)
    # Time In:
    time_in_thu = models.TimeField(blank=True, null=True)
    # Time Out:
    time_out_thu = models.TimeField(blank=True, null=True)
    # If lunch == "Yes": -0.30 (or -30 min) to hours
    lunch_thu = models.CharField(max_length=4, choices=LUNCH, default="")
    # Vehicle:
    vehicles_thu = models.CharField(max_length=250, blank=True, null=True)
    # Job Addr + Desc:
    job_address_thu = models.CharField(max_length=250, blank=True, null=True)
    job_description_thu = models.CharField(max_length=250, blank=True, null=True)
    # Total hours:
    hours_thu = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)


    ## FRI: ##
    # Date:
    date_fri = models.DateField(blank=True, null=True)
    # Time In:
    time_in_fri = models.TimeField(blank=True, null=True)
    # Time Out:
    time_out_fri = models.TimeField(blank=True, null=True)
    # If lunch == "Yes": -0.30 (or -30 min) to hours
    lunch_fri = models.CharField(max_length=4, choices=LUNCH, default="")
    # Vehicle:
    vehicles_fri = models.CharField(max_length=250, blank=True, null=True)
    # Job Addr + Desc:
    job_address_fri = models.CharField(max_length=250, blank=True, null=True)
    job_description_fri = models.CharField(max_length=250, blank=True, null=True)
    # Total hours:
    hours_fri = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)

    ## SAT: ##
    # Date:
    date_sat = models.DateField(blank=True, null=True)
    # Time In:
    time_in_sat = models.TimeField(blank=True, null=True)
    # Time Out:
    time_out_sat = models.TimeField(blank=True, null=True)
    # If lunch == "Yes": -0.30 (or -30 min) to hours
    lunch_sat = models.CharField(max_length=4, choices=LUNCH, default="")
    # Vehicle:
    vehicles_sat = models.CharField(max_length=250, blank=True, null=True)
    # Job Addr + Desc:
    job_address_sat = models.CharField(max_length=250, blank=True, null=True)
    job_description_sat = models.CharField(max_length=250, blank=True, null=True)
    # Total hours:
    hours_sat = models.DecimalField(decimal_places=2, max_digits=4, blank=True, null=True)

    def __str__(self):
        return str(self.time_sheet_week_from) + ' - ' + str(self.time_sheet_week_to) + ' by ' + str(self.employee)