from django.shortcuts import render
from django.views import View


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

    # def post(self, request, *args, **kwargs):
    #     '''
    #     posts date picker form data
    #     '''
    #     date_picker_form = DatePickerForm(data=request.POST)

    #     if date_picker_form.is_valid():
    #         date_picked_instance = date_picker_form.save(commit=False)
    #         date_picked_instance.save()
    #         slug = date_picked_instance.slug
    #         return redirect("visits:day_report", slug)
    #     else:
    #         slug = request.POST.get("date_picked")
    #         return redirect("visits:day_report", slug)