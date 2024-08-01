from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable":"My name is Neel"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Home page")

def about(request):
    return render(request, 'about.html')

    # return HttpResponse("This is About page")

def service(request):
    return render(request, 'service.html')

    # return HttpResponse("This is Service page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, phone=phone, email=email, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent! Thank you")


    return render(request, 'contact.html')

    # return HttpResponse("This is Contact page")        