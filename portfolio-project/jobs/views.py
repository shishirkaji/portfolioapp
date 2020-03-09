from django.shortcuts import render
from .models import Job

def shishir(request):
    return render(request, 'jobs/shishir.html')

def home(request):
    jobs= Job.objects
    return render( request , 'jobs/home.html', {'jobs':jobs})