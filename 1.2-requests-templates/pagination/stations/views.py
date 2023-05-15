from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv
from pagination.settings import BUS_STATION_CSV as base


def index(request):
    return redirect(reverse('bus_stations'))

def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    CONTENT = []
    with open(f'{base}', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for el in reader:
            CONTENT.append(el)
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    station = paginator.get_elided_page_range()
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)