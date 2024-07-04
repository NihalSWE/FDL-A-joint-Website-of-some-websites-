from django.contrib import admin
from .models import Portfolio,CarouselItem,BusinessStrength,CareerApplication,Career_HeaderImage


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id','file','uploaded_at']


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']

@admin.register(BusinessStrength)
class BusinessStrengthAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'icon', 'link']







@admin.register(Career_HeaderImage)
class Career_HeaderImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
    search_fields = ('id',)

@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'address', 'message','cv','submitted_at',)
    search_fields = ('name', 'number', 'address',)