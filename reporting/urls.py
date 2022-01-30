from django.urls import path
from . import views

urlpatterns = [

    path('date_picker', views.DatePickerView.as_view(), name='date_picker'),

    # path('test', views.get_mood_report_page, name='test_mood_report'),

]
