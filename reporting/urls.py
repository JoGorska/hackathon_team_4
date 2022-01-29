from django.urls import path
from . import views

urlpatterns = [

    path('reporting/datepicker', views.DatePicker.as_view(), name='date_picker'),
    path('reporting/<slug:date_start>/<slug:date_end>', views.ReportMoodView.as_view(), name='report_mood'),
]
