from django.shortcuts import render, redirect
from .models import TimeForm
from .forms import TimeFormForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'timesheet_app/index.html', {})


@login_required
def add_form(request):
    if request.method == "POST":
        form = TimeFormForm(request.POST)
        if form.is_valid():
            emp = form.save(commit=False)
            emp.employee = request.user
            emp.save()
            return redirect('timesheet_app:add_form')
        else:
            return redirect('timesheet_app:index')
    else:
        form = TimeFormForm()
    return render(request, 'timesheet_app/add_form.html', {'form': form})
