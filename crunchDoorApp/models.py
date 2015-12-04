from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 50)
    website = models.CharField(max_length = 100, default='0')
    total_Reviews = models.IntegerField(default=0)
    average = models.DecimalField(max_digits = 3, decimal_places = 2 , default =0)
    logo = models.CharField(max_length = 200, default='0')
    industry = models.CharField(max_length = 50, default='0')

class CrunchMemoized(models.Model):
	permalink = models.CharField(max_length = 150, unique=True)
	short_description = models.CharField(max_length= 400)

class LocationMemoized(models.Model):
	permalink = models.CharField(max_length = 150)
	name = models.CharField(max_length = 50, null=True)
	street_1 = models.CharField(max_length = 50, null=True)
	city = models.CharField(max_length = 50, null=True)

class ProductMemoized(models.Model):
	permalink = models.CharField(max_length = 150)
	name = models.CharField(max_length = 50)
