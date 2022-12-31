from django.contrib import admin
from .models.product import Product
from .models.categories import Categories
from .models.book import Book
from .models.b_catogeries import B_categories


class Book_display(admin.ModelAdmin):
    list_display = ['name', 'a_uth', 'desc', 'b_categories']
    
class B_categories_display(admin.ModelAdmin):
    list_display = ['name','id']

class product_display(admin.ModelAdmin):
    list_display = ['name', 'price', 'desc', 'categories']
    
class categories_display(admin.ModelAdmin):
    list_display = ['name','id']


# Register your models here.
admin.site.register(Product, product_display)
admin.site.register(Categories,categories_display)
admin.site.register(Book,Book_display)
admin.site.register(B_categories,B_categories_display)
admin.site.site_header = "[ Admin ] Ink Spot"
