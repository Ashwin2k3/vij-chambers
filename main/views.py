from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Blog, Testimonial

# def index(request):
#     return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def index(request):
    blogs = Blog.objects.all()[:3]  # Display the latest 3 blogs or adjust as needed
    return render(request, 'index.html', {'blogs': blogs})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})

def book_appointment(request):
    return render(request, 'appointment.html')

def about(request):
    return render(request, 'about.html')

# main/views.py

# main/views.py

from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': blogs})


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Send email
        subject = 'Contact Form Submission'
        email_message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
        send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

        return HttpResponseRedirect(reverse('contact_success'))

    return render(request, 'appointment.html')