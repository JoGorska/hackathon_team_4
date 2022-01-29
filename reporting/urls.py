from django.urls import path
from . import views

urlpatterns = [

    path('date_picker', views.DatePickerView.as_view(), name='date_picker'),
    # path('report_mood', views.ReportMoodView.as_view(), name='report_mood'),
]
