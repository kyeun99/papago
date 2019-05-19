from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'blog/home.html')

def detail(request):
    return render(request, 'blog/detail.html')

def orderlist(request):
    return render(request, 'blog/orderlist.html')