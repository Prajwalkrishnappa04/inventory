from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Item  # Import your model

admin.site.register(Item)  # Register it with the admin
