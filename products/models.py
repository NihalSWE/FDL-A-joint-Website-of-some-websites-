from django.db import models

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