from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1><a href="/first01/test">Hello. Django!</a></h1>')

def test(request):
    return HttpResponse('<h1><a href="/first01">return</a></h1>')