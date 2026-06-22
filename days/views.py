from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# from django.template.loader import render_to_string


days = {
    'saturday': 'Saturday in Dictionary',
    'sunday': 'sunday in dictionary',
    'monday': 'monday in dictionary',
    'tuesday': 'Tuesday in Dictionary',
    'wednesday': 'Wednesday in Dictionary',
    'thursday': 'Thursday in Dictionary',
    'friday': ''
}

day_list = list(days.keys())


def dynamic_days(request, day):
    day_data = days.get(day)
    # -> dares 14 -> render template + template filters + template tags

    context = {
        'day': day,
        'day_data': day_data
    }
    return render(request, 'days/day_info.html', context)


def index(request):
    # -> dars 15 -> template tags initially
    context = {
        'days': day_list
    }
    return render(request, "days/days.html", context)



def dynamic_days_by_number(request, day_number):
    if day_number > len(day_list):
        return HttpResponseNotFound('the day number not exist in day numbers')
    day = day_list[day_number - 1]
    url_path = reverse('dynamic_days', args=[day])
    return HttpResponseRedirect(url_path)
