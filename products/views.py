from django.shortcuts import render, redirect

from django.contrib import messages
from .models import Portfolio,CarouselItem,BusinessStrength,CareerApplication,Career_HeaderImage
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



def career(request):
    header_image = Career_HeaderImage.objects.first()  # Retrieve header image

    context = {
        'header_image': header_image,
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        address = request.POST.get('address')
        message = request.POST.get('message')
        cv = request.FILES.get('cv')

        if name and email and number and address and message and cv:
            # Save the career application
            application = CareerApplication(
                name=name,
                email=email,
                number=number,
                address=address,
                message=message,
                cv=cv
            )
            application.save()

            # Add success message
            messages.success(request, 'Your application has been submitted successfully.')

            return redirect('career')  # Redirect to the career page
        else:
            # Add error message if form is not valid
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'products/career.html', context)

