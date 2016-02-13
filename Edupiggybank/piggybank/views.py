from django.shortcuts import render

def passbook_list(request):
    return render(request, 'piggybank/passbook_list.html', {})
# Create your views here.
