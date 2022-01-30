from django.urls import path
from . import views

urlpatterns = [

    path('date_picker', views.DatePickerView.as_view(), name='date_picker'),
    # path('report_mood', views.ReportMoodView.as_view(), name='report_mood'),
    path('test', views.get_mood_report_page, name='test_mood_report'),
    path('test-404', views.get_test_404_page, name='test_404_page'),
]
