from django.shortcuts import render
from .models import Portfolio,CarouselItem,BusinessStrength
# Create your views here.
def base(request):
    return render(request, 'products/base.html')


def home(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    carousel_items = CarouselItem.objects.all()
    business_strengths = BusinessStrength.objects.all()
    context = {
        'portfolio': portfolio,
        'carousel_items': carousel_items,
        'business_strengths': business_strengths
    }
    return render(request, 'products/home.html',context)

def about(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'products/about.html',context)

def service(request):
    business_strengths = BusinessStrength.objects.all()
    context = {
        'business_strengths': business_strengths
    }

    return render(request,'products/service.html',context)