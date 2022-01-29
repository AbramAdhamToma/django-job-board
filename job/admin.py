from django.contrib import admin

# Register your models here.
from .models import Job

admin.site.register(Job)# make admin panel see job app