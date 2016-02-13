from django.shortcuts import render
from django.utils import timezone
from .models import Passbook
from .forms import PassbookForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def index(request):
    return render(request, 'piggybank/index.html', {})
def mypassbook(request):
    entries = Passbook.objects.all()
    return render(request, 'piggybank/mypassbook.html',{'entries':entries})
def transaction(request):
    if request.method == "POST":
        form = PassbookForm(request.POST)#doubt
        if form.is_valid():
            passbook = form.save(commit=False)
            passbook.save()
            return redirect('transaction_detail', pk=passbook.pk)
    else:
        form = PassbookForm()
    return render(request, 'piggybank/transaction_edit.html', {'form': form})
def transaction_detail(request,pk):
    post = get_object_or_404(Passbook, pk=pk)
    return render(request,'piggybank/transaction_detail.html',{'passbook':post})
def transaction_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('transaction_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'piggybank/transaction_edit.html', {'form': form})

