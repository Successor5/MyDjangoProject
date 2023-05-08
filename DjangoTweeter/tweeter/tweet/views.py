from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def welcome1(request):
    return HttpResponse("welcome to django")


def welcome(request):
    return render(request, "tweet/template/home.html")