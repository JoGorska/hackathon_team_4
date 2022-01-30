from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from wellbeing.models import Mood


class DatePickerView(View):
    '''
    Date picker that allows the user to choose which day to display
    than redirects to mood report table containing data from database
    '''
    template_name = "reporting/date_picker.html"

    def get(self, request, *args, **kwargs):
        '''
        gets page that displays a html form
        '''
        return render(request, 'reporting/date_picker.html')

    def post(self, request, *args, **kwargs):
        '''
        posts date picker form data
        '''
        # gets data posted by the html form
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        user_id = request.POST.get('user_id')
        # gets user object
        user = get_object_or_404(User, id=user_id)
        # filters all Mood Model objects from the date range for this user
        mood_objects_list = Mood.objects.filter(created_on__range=[start_date, end_date]).filter(author=user)

        # creates lists
        list_of_dates = []
        list_of_dates_strings = []
        # for loop to get list of dates
        for object in mood_objects_list:
            date_object = object.created_on
            date_to_string = date_object.strftime("%d %B %Y")
            if date_to_string not in list_of_dates_strings:
                list_of_dates_strings.append(date_to_string)
                list_of_dates.append(date_object)

        list_of_moods_in_one_day = []
        dict_date_moods = {}
        # for loop to get list of moods
        for date_object in list_of_dates:

            date_to_string = date_object.strftime("%d %B %Y")
            moods_objects_on_day = Mood.objects.filter(created_on=date_object).filter(author=user)
            for object in moods_objects_on_day:
                mood = object.mood
                if mood not in list_of_moods_in_one_day:
                    list_of_moods_in_one_day.append(mood)
            # creates key value pair
            date_and_moods = {date_to_string: list_of_moods_in_one_day}
            # adds item to dictionary: date as key and list of moods as value
            dict_date_moods.update(date_and_moods)
        context = {'dict_date_moods': dict_date_moods,}
        return render(request, 'reporting/mood_report.html', context)


# def get_mood_report_page(request):
#     """ View to get mood report page """
#     return render(request, 'reporting/mood_report.html')
