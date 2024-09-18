from django.urls import path, include 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:id>/', views.blog_detail, name='blog_detail'),
    path('about/', views.about, name='about'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('appointment/', views.book_appointment, name='appointment'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
