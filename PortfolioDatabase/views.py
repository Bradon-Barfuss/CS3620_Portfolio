from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio
from .models import Hobbies

# Create your views here.
def home(request):
    return HttpResponse("""Hi! <br> My Name is bradon barfuss! I am a highly motivated Computer Scientist specializing in software development and machine learning. 
Experience in full-stack development, UI/UX design, Object-Oriented Programming, and cloud-based 
development. Strong background in collaborative team environments, coding, testing, and deployment 
across various platforms using SDLC. """)

def hobbies(request):
    return HttpResponse(Hobbies.objects.all())

def portfolio(request):
    return HttpResponse(Portfolio.objects.all())

def contact(request):
    return HttpResponse("bradonbarfuss@mail.weber.edu")
