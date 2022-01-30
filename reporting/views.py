from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from wellbeing.models import Mood


class DatePickerView(View):
    '''
    Date picker that allows the user to choose which day to display
    successfull url redirects to the page where url contains date
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
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        # need to add one day to end date ???
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, id=user_id)
        mood_objects_list = Mood.objects.filter(created_on__range=[start_date, end_date]).filter(author=user)
        list_of_dates = []
        list_of_dates_strings = []
        for object in mood_objects_list:
            date = object.created_on
            date_to_string = date.strftime("%d %B %Y")
            list_of_dates_strings.append(date_to_string)
            list_of_dates.append(date)
            unique_dates_list = list(set(list_of_dates))

        print(f'DATE OF OBJECT{unique_dates_list}')
        for date in unique_dates_list:
            moods_objects_on_day = Mood.objects.filter(created_on=date)
            print(f'THIS IS ONE DATE{date}')
            


        # context = {
        #     start_date = start_date
        #     end_date = end_date
        # }
        # return redirect("reports:mood_report", context)
        return render(request, 'index.html')


def get_mood_report_page(request):
    """ View to get mood report page """
    return render(request, 'reporting/mood_report.html')


def get_test_404_page(request):
    """ View to get 404 page page """
    return render(request, '404.html')
