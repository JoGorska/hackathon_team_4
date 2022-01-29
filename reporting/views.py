from django.shortcuts import render
from django.views import View
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
        
        mood_objects_list = Mood.objects.filter(created_on__range=[start_date, end_date])
        print(f'MOOD OBJECTS_LIST IN DATE RANGE {mood_objects_list}')
        list_of_dates = []
        for object in mood_objects_list:
            date = object.created_on
            date_to_words = date.strftime("%d %B %Y")
            list_of_dates.append(date_to_words)
            unique_dates_list = list(set(list_of_dates))
            print(f'DATE OF OBJECT{unique_dates_list}')
            moods_objects_on_day = Mood.objects.filter(created_on=date)

        # context = {
        #     start_date = start_date
        #     end_date = end_date
        # }
        # return redirect("reports:mood_report", context)
        return render(request, 'index.html')