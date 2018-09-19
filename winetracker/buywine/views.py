from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Varietal, Winery, Vintner


def index(request):
    return render(request, 'buywine/index.html')

def save_new_wine_purchase(request):
    context = {
        'varietals': Varietal.objects.get_queryset().filter(visible=True),
        'wineries': Winery.objects.get_queryset().filter(visible=True),
        'vintners': Vintner.objects.get_queryset().filter(visible=True),
    }
    return render(request, 'buywine/save_new_wine_purchase.html', context=context)

def save_wine_details(request):
    return HttpResponse("Displaying edited details for particular wine")

def find_wine(request):
    return HttpResponse("Searching for wine now...")

def display_wine_details(request):
    return HttpResponse("Displaying details for particular wine  ")

def explore_wine_collection(request):
    return HttpResponse("Exploring wine collection!")




