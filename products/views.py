from django.shortcuts import render
from .models import Portfolio
# Create your views here.
def base(request):
    return render(request, 'products/base.html')


def home(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'products/home.html',context)

def about(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'products/about.html',context)