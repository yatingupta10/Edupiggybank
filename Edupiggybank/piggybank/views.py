from django.shortcuts import render

def index(request):
    return render(request, 'piggybank/index.html', {})
def mypassbook(request):
    return render(request, 'piggybank/mypassbook.html')
# Create your views here.
