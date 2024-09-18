from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Testimonial, Appointment

admin.site.register(Blog)
admin.site.register(Testimonial)
admin.site.register(Appointment)
