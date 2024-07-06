from django.contrib import admin
from .models import Portfolio,CarouselItem,BusinessStrength,CareerApplication,ContactStaticContent, ContactFormData,TeamMember,Investor


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id','file','uploaded_at']


@admin.register(CarouselItem)
class CarouselItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image']

@admin.register(BusinessStrength)
class BusinessStrengthAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'image', 'icon', 'link']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('name', 'position')
    search_fields = ('name', 'position')








@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'address', 'message','cv','submitted_at',)
    search_fields = ('name', 'number', 'address',)



@admin.register(ContactStaticContent)
class ContactStaticContentAdmin(admin.ModelAdmin):
    list_display = ('heading', 'subheading', 'description',)
    search_fields = ('heading', 'subheading',)

@admin.register(ContactFormData)
class ContactFormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at',)
    search_fields = ('name', 'subject',)