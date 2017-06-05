import json
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from FoodTrucker.models import Schedule
from django.template import RequestContext
from datetime import datetime

#function that returns a json list of foodtrucks for a given date
def getFoodTrucks(date):
    foodtrucks = Schedule.objects.filter(startDateTime__day=date.day)
    return foodtrucks

# Create your views here.
def index(request):

    if request.is_ajax():
        newDate = request.POST.get('date')
        newDateTime = datetime.strptime(newDate, '%Y-%m-%d')
        foodtrucks = getFoodTrucks(newDateTime)

        newContext = {
            'foodtrucks': foodtrucks,
        }

        return HttpResponse(newContext)

    today = datetime.now()
    # endofWeek = today + timedelta(days=6)
    foodtrucks = getFoodTrucks(today)

    context = {
        "foodtrucks": foodtrucks,
    }
    return render(request, 'FoodTrucker/index.html', context)