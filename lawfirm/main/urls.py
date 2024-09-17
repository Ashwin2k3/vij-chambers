from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('blogs/', views.blogs, name='blogs'),
    path('appointment/', views.book_appointment, name='appointment'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
