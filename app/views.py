from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Data_URL(request,data):
    return HttpResponse(f'<center><h1>This is collected data from url->->-><i>{data}</i></h1></center>')