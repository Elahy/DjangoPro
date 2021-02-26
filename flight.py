from django.http import HttpResponse
from django.shortcuts import render

#views here
def index(request):
  return HttpResponse("Hello, world!")
