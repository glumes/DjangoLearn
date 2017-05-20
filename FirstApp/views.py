# Create your views here.
# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u'Hello World')


def home(request):
    string = "use data in template"

    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]

    return render(request, 'firstapp/home.html', {'string': string, "TutorialList": TutorialList})
