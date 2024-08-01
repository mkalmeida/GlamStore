from django.contrib import admin

# show category table on admin page
from .models import Category, Item 

admin.site.register(Category)
admin.site.register(Item)

