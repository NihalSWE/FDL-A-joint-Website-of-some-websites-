from django.db import models
from django.utils import timezone

class Portfolio(models.Model):
    file = models.FileField(upload_to='portfolios/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Portfolio uploaded on {self.id}"

class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=300)

    def __str__(self):
        return self.title
    
class BusinessStrength(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='business_strength/')
    icon = models.ImageField(upload_to='business_strength/icons/')
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    

class Franchise(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='franchise/')
    icon=models.ImageField(upload_to='franchise/icons')
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class CareerApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    message = models.TextField()
    cv = models.FileField(upload_to='cvs/')
    submitted_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class ContactStaticContent(models.Model):
    heading = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    map_embed_url = models.TextField()  # Store the full iframe code

    def __str__(self):
        return self.heading
    

class ContactFormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
    
class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('Chairman', 'Chairman'),
        ('MD', 'Managing Director'),
        # Add more roles as needed
    ]
    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    bio = models.TextField(blank=True, null=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='Chairman')
   
    def __str__(self):
        return self.name
    

from django.db import models
from PIL import Image
import os

class Investor(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    quote = models.TextField(max_length=150)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Call the original save method
        super().save(*args, **kwargs)

        # Resize the image if it exists
        if self.image and hasattr(self.image, 'path'):
            image_path = self.image.path
            # Open and resize the image
            with Image.open(image_path) as img:
                size = (300, 300)  # Square dimensions
                img = img.resize(size, Image.LANCZOS)
                
                # Save the resized image
                img.save(image_path)

    
    

class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return self.title
    

from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title