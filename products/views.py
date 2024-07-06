from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Portfolio,CarouselItem,BusinessStrength,CareerApplication,ContactStaticContent, ContactFormData,TeamMember,Investor
# Create your views here.
def base(request):
    return render(request, 'products/base.html')


def home(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    carousel_items = CarouselItem.objects.all()
    business_strengths = BusinessStrength.objects.all()
    team_members = TeamMember.objects.all()
    investors = Investor.objects.all()
    context = {
        'portfolio': portfolio,
        'carousel_items': carousel_items,
        'business_strengths': business_strengths,
        'team_members': team_members,
        'investors': investors
    }
    return render(request, 'products/home.html',context)

def about(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'products/about.html',context)

def service(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    business_strengths = BusinessStrength.objects.all()
    context = {
        'portfolio': portfolio,
        'business_strengths': business_strengths
    }

    return render(request,'products/service.html',context)



def career(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    

    context = {
        'portfolio': portfolio,
        
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

def contact(request):
    portfolio = Portfolio.objects.last()  # Get the most recently uploaded portfolio
    static_content = ContactStaticContent.objects.first()  # Assuming there's only one record

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save form data to the database
        ContactFormData.objects.create(name=name, email=email, subject=subject, message=message)

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')  # Redirect to the same page or another page


    context = {
        'portfolio': portfolio,
        'static_content': static_content
        
    }
    return render(request,'products/contact.html', context)

