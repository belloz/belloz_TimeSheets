from django import forms
from .models import TimeForm
from django.contrib.admin import widgets

class TimeFormForm(forms.ModelForm):
    class Meta:

        model = TimeForm
        fields = (
            'total_week_hours',
            'time_sheet_week_from',
            'time_sheet_week_to',
            # MONDAY:
            'date_mon',
            'time_in_mon',
            'time_out_mon',
            'lunch_mon',
            'vehicles_mon',
            'job_address_mon',
            'job_description_mon',
            'C',

            # TUE:
            'date_tue',
            'time_in_tue',
            'time_out_tue',
            'lunch_tue',
            'vehicles_tue',
            'job_address_tue',
            'job_description_tue',
            'hours_tue',

            # WED:
            'date_wed',
            'time_in_wed',
            'time_out_wed',
            'lunch_wed',
            'vehicles_wed',
            'job_address_wed',
            'job_description_wed',
            'hours_wed',

            # THU:
            'date_thu',
            'time_in_thu',
            'time_out_thu',
            'lunch_thu',
            'vehicles_thu',
            'job_address_thu',
            'job_description_thu',
            'hours_thu',

            # FRI:
            'date_fri',
            'time_in_fri',
            'time_out_fri',
            'lunch_fri',
            'vehicles_fri',
            'job_address_fri',
            'job_description_fri',
            'hours_fri',

            # SAT:
            'date_sat',
            'time_in_sat',
            'time_out_sat',
            'lunch_sat',
            'vehicles_sat',
            'job_address_sat',
            'job_description_sat',
            'hours_sat',

        )

        widgets = {
            'total_week_hours': forms.NumberInput(attrs={'id': 'total_week_hours', 'class': 'form-control', 'readonly': True}),
            'time_sheet_week_from': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_sheet_week_to': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),

            ## MONDAY:
            'date_mon': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_in_mon': forms.TimeInput(attrs={'id': 'time_in_mon', 'class': 'form-control', 'placeholder': ''}),
            'time_out_mon': forms.TimeInput(attrs={'id': 'time_out_mon', 'class': 'form-control', 'placeholder': ''}),
            'lunch_mon': forms.Select(attrs={'id': 'lunch_mon', 'class': 'form-control'}),
            'vehicles_mon': forms.TextInput(attrs={'class': 'form-control'}),
            'job_address_mon': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description_mon': forms.TextInput(attrs={'class': 'form-control'}),
            'C': forms.NumberInput(attrs={'id': 'C', 'class': 'form-control'}),

            ## TUE:
            'date_tue': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_in_tue': forms.TimeInput(attrs={'id': 'time_in_tue', 'class': 'form-control', 'placeholder': ''}),
            'time_out_tue': forms.TimeInput(attrs={'id': 'time_out_tue', 'class': 'form-control', 'placeholder': ''}),
            'lunch_tue': forms.Select(attrs={'id': 'lunch_tue', 'class': 'form-control'}),
            'vehicles_tue': forms.TextInput(attrs={'class': 'form-control'}),
            'job_address_tue': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description_tue': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_tue': forms.NumberInput(attrs={'id': 'hours_tue', 'class': 'form-control'}),

            ## WED:
            'date_wed': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_in_wed': forms.TimeInput(attrs={'id': 'time_in_wed', 'class': 'form-control', 'placeholder': ''}),
            'time_out_wed': forms.TimeInput(attrs={'id': 'time_out_wed', 'class': 'form-control', 'placeholder': ''}),
            'lunch_wed': forms.Select(attrs={'id': 'lunch_wed', 'class': 'form-control'}),
            'vehicles_wed': forms.TextInput(attrs={'class': 'form-control'}),
            'job_address_wed': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description_wed': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_wed': forms.NumberInput(attrs={'id': 'hours_wed', 'class': 'form-control'}),

            ## THU:
            'date_thu': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_in_thu': forms.TimeInput(attrs={'id': 'time_in_thu', 'class': 'form-control', 'placeholder': ''}),
            'time_out_thu': forms.TimeInput(attrs={'id': 'time_out_thu', 'class': 'form-control', 'placeholder': ''}),
            'lunch_thu': forms.Select(attrs={'id': 'lunch_thu', 'class': 'form-control'}),
            'vehicles_thu': forms.TextInput(attrs={'class': 'form-control'}),
            'job_address_thu': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description_thu': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_thu': forms.NumberInput(attrs={'id': 'hours_thu', 'class': 'form-control'}),


            ## FRI:
            'date_fri': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_in_fri': forms.TimeInput(attrs={'id': 'time_in_fri', 'class': 'form-control', 'placeholder': ''}),
            'time_out_fri': forms.TimeInput(attrs={'id': 'time_out_fri', 'class': 'form-control', 'placeholder': ''}),
            'lunch_fri': forms.Select(attrs={'id': 'lunch_fri', 'class': 'form-control'}),
            'vehicles_fri': forms.TextInput(attrs={'class': 'form-control'}),
            'job_address_fri': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description_fri': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_fri': forms.NumberInput(attrs={'id': 'hours_fri', 'class': 'form-control'}),


            ## SAT:
            'date_sat': forms.DateInput(format='%Y-%m-%d',
                                        attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'time_in_sat': forms.TimeInput(attrs={'id': 'time_in_sat', 'class': 'form-control', 'placeholder': ''}),
            'time_out_sat': forms.TimeInput(attrs={'id': 'time_out_sat', 'class': 'form-control', 'placeholder': ''}),
            'lunch_sat': forms.Select(attrs={'id': 'lunch_sat', 'class': 'form-control'}),
            'vehicles_sat': forms.TextInput(attrs={'class': 'form-control'}),
            'job_address_sat': forms.TextInput(attrs={'class': 'form-control'}),
            'job_description_sat': forms.TextInput(attrs={'class': 'form-control'}),
            'hours_sat': forms.NumberInput(attrs={'id': 'hours_sat', 'class': 'form-control'}),

        }
