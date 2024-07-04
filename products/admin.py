from django.contrib import admin
from .models import Portfolio,CarouselItem,BusinessStrength

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id','file','uploaded_at']


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']

@admin.register(BusinessStrength)
class BusinessStrengthAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'icon', 'link']