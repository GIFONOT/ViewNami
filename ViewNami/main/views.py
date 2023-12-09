from django.shortcuts import render
from django.http import HttpResponse

def index(rec):
    return render(rec, 'main/animes.html')
 