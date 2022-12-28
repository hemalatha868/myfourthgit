from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>my first view in app1</h1>')


def second(request):
    return HttpResponse('<h1>my second view in app1</h1>')
