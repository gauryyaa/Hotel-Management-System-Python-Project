from django.shortcuts import render
from datetime import datetime
from h_app. models import Register
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        aadhaar = request.POST.get('aadhaar')
        room = request.POST.get('room')
        days = request.POST.get('days')
        register = Register(name=name, email=email, phone=phone, aadhaar=aadhaar, room=room, days=days)
        register.save()
        messages.success(request, 'Your Details have been sent.')
    return render(request,'register.html')
