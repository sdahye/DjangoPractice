from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hello, World!</h1><a href="/first01">first01</a>')