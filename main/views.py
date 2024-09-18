# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from .models import Blog, Testimonial

# # def index(request):
# #     return render(request, 'index.html')

# def services(request):
#     # Fetch all service entries from the database
#     services_list = Service.objects.all()
#     # Pass the services list to the template
#     return render(request, 'services.html', {'services': services_list})

# def index(request):
#     blogs = Blog.objects.all()[:3]  # Display the latest 3 blogs or adjust as needed
#     return render(request, 'index.html', {'blogs': blogs})

# def blogs(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blogs.html', {'blogs': blogs})

# def book_appointment(request):
#     return render(request, 'appointment.html')

# def about(request):
#     return render(request, 'about.html')

# # main/views.py

# # main/views.py

# from django.shortcuts import render, get_object_or_404
# from .models import Blog

# def blog_detail(request, id):
#     blog = get_object_or_404(Blog, id=id)
#     return render(request, 'blog_detail.html', {'blog': blog})

# def blogs(request):
#     blogs = Blog.objects.all()
#     return render(request, 'blogs.html', {'blogs': blogs})


# def service_detail(request, slug):
#     service = get_object_or_404(Service, slug=slug)
#     return render(request, 'service_detail.html', {'service': service})


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name', '')
#         email = request.POST.get('email', '')
#         message = request.POST.get('message', '')

#         # Send email
#         subject = 'Contact Form Submission'
#         email_message = f'Name: {name}\nEmail: {email}\nMessage: {message}'
#         send_mail(subject, email_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

#         return HttpResponseRedirect(reverse('contact_success'))

#     return render(request, 'appointment.html')

from django.shortcuts import render, get_object_or_404
from .models import Blog, Testimonial, Service  # Ensure Service is imported
from django.core.mail import send_mail  # Import for sending emails
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings  # Import settings to use DEFAULT_FROM_EMAIL

def services(request):
    # Fetch all service entries from the database
    services_list = Service.objects.all()
    # Pass the services list to the template
    return render(request, 'services.html', {'services': services_list})

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

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': blog})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'service_detail.html', {'service': service})

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
