from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Blog, Testimonial

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def book_appointment(request):
    return render(request, 'appointment.html')
