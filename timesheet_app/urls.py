from django.conf.urls import url
from . import views


app_name = "timesheet_app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_form/$', views.add_form, name='add_form'),
]
