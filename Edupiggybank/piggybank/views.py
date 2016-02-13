from django.shortcuts import render
from django.utils import timezone
from .models import Passbook

def index(request):
    return render(request, 'piggybank/index.html', {})
def mypassbook(request):
    entries = Passbook.objects.all()
    return render(request, 'piggybank/mypassbook.html',{'entries':entries})
# Create your views here.
