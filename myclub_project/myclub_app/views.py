# from django.shortcuts import render
#
# # Create your views here.
# from datetime import datetime
# from django.http import HttpResponse
#
# def show_the_time(request):
#     now = datetime.now()
#     html = "<html><body>Hello World</body></html>".format(now)
#     return HttpResponse(html)
#

from datetime import datetime
from django.http import HttpResponse
from django.views import View  # Import the View parent class
from django.views.generic.list import ListView
from .models import Event

class ShowTimeView(View):  # Create a view class

    # Change the function-based view to be called get and add the self param
    def get(self, request):
        now = datetime.now()
        events_list = list(Event.objects.all().values_list('name', flat=True))
        html = "<html><body>{}</body></html>".format(events_list)
        return HttpResponse(html)
