# from django.db import models

# # Create your models here.
# from django.db import models

# # main/models.py

# from django.db import models

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='blog_images/', blank=True, null=True)  # Optional image field
    
#     def __str__(self):
#         return self.title


# class Testimonial(models.Model):
#     name = models.CharField(max_length=100)
#     text = models.TextField()

# class Appointment(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     message = models.TextField()
#     date = models.DateTimeField(auto_now_add=True)

# # main/models.py

# from django.db import models

# class Service(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     detailed_description = models.TextField()  # For the detailed service page
#     image = models.ImageField(upload_to='image_services/')
#     slug = models.SlugField(unique=True)  # Slug for detailed page URL

#     def __str__(self):
#         return self.title



# main/models.py
from django.db import models

# Create your models here.
from django.db import models

# main/models.py

from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # Use RichTextField instead of TextField
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    text = RichTextField()  # Use RichTextField instead of TextField

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = RichTextField()  # Use RichTextField instead of TextField
    date = models.DateTimeField(auto_now_add=True)

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()  # Use RichTextField instead of TextField
    detailed_description = RichTextField()  # Use RichTextField instead of TextField
    image = models.ImageField(upload_to='image_services/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
