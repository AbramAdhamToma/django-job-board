from unicodedata import category
from django.contrib import admin

# Register your models here.
from .models import Job, Category

admin.site.register(Job)# make admin panel see job app
# admin.site.register(Category)

admin.site.register(Category)