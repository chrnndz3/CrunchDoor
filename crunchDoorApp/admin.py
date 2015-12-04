from django.contrib import admin

from .models import Company, CrunchMemoized, LocationMemoized, ProductMemoized, Crunch

# class CompanyAdmin(admin.ModelAdmin):
# 	fields = ['numberofEmployees', 'date_founded', 'description', 'name', 'total_funding', 'website']

# class ContactAdmin(admin.ModelAdmin):
# 	fields = ['company', 'email_address', 'phone_number', 'address']

# class ReviewAdmin(admin.ModelAdmin):
# 	fields = ['company', 'total_Reviews', 'average']

# class LocationAdmin(admin.ModelAdmin):
# 	fields = ['company', 'lattitude', 'longitude']

admin.site.register(Company)
admin.site.register(CrunchMemoized)
admin.site.register(LocationMemoized)
admin.site.register(ProductMemoized)
admin.site.register(Crunch)
# Register your models here.
