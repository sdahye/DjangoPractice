from django.shortcuts import render

# Create your views here.
def hello(request):
    return render(request, 'first02.html', {'name': 'dahye'})

def variable01(request):
    lst = ['Dan', 'Diana', 'Gabe', 'Natalie']
    return render(request, 'variable01.html', {'lst': lst})

def variable02(request):
    dct = {'class': '2', 'name': 'sdh'}
    return render(request, 'variable02.html', {'dct': dct})