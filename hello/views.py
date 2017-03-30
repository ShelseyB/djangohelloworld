from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCount
# Create your views here.





def index(request):
    row, created = PageCount.objects.get_or_create(page = 'index')
    row.visits = row.visits + 1
    row.save()
    if created:
        words = "You are the 1st visitor!"
    else:
        words = "You are visitor #"+str(row.visits)
    return HttpResponse("Hello, world! It's " + time.strftime('%c') + "\n" + words)