# from django.contrib import admin

# # Register your models here.
# from django.contrib import admin
# from .models import Blog, Testimonial, Appointment, Service



# admin.site.register(Blog)
# admin.site.register(Testimonial)
# admin.site.register(Appointment)
# admin.site.register(Service)

# main/admin.py

from django.contrib import admin
from .models import Blog, Testimonial, Appointment, Service
from ckeditor.widgets import CKEditorWidget
from django import forms

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }

class ServiceAdminForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'description': CKEditorWidget(),
            'detailed_description': CKEditorWidget(),
        }

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    form = ServiceAdminForm
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Testimonial)
admin.site.register(Appointment)
