from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template

def home(request):
    return render(request, 'index.html')
def hello(request):
    return HttpResponse ('Hello World!', content_type="text/plain")
def static(request):
    return render(request, 'static_handler.html')
# Create your views here.
