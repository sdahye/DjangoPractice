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

def forLoop(request):
    return render(request, 'for.html', {'number': range(0,10)})

def if01(request):
    return render(request, 'if01.html', {'user':{'id':'2', 'name':'SDH'}})

def if02(request):
    return render(request, 'if02.html', {'role': 'manager'})
