from django.http import HttpResponseNotFound, HttpResponseRedirect , Http404
from django.shortcuts import render
from django.template.loader import render_to_string
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
    if day_data is None:
        raise Http404()
        # page_not_found = render_to_string('404.html')
        # return HttpResponseNotFound(page_not_found)

    context = {
        'day': day,
        'day_data': day_data
    }
    return render(request, 'days/day_info.html', context)


def index(request):
    context = {
        'days': day_list
    }
    return render(request, "days/days.html", context)


def dynamic_days_by_number(request, day_number):
    if day_number > len(day_list):
        return HttpResponseNotFound('the day number not exist')
    day = day_list[day_number - 1]
    url_path = reverse('dynamic_days', args=[day])
    return HttpResponseRedirect(url_path)
