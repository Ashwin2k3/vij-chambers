# main/forms.py

from django import forms
from .models import Blog
from .models import Testimonial

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'image']

class TestimonialForm(forms.ModelForm):
    class Meta: 
        model = Testimonial
        fields = ['name', 'text']
        
  
class AppointmentForm(forms.ModelForm):
    class Meta : 
        model = Appointment
        fields = ['name','email', 'message', 'date']      
