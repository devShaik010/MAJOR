from django.db import models
from .categories import Categories

# this is for product card items 
class Product(models.Model):
    name = models.CharField(max_length=20)
    discount = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=40)
    image = models.ImageField(upload_to="Uploads\product")
    categories = models.ForeignKey(Categories,on_delete=models.CASCADE, default=1)

   #storing data in function 
    @staticmethod
    def get_all():
        return Product.objects.all()

    @staticmethod
    def get_all_filter(category_1):
        if category_1:
         return Product.objects.filter(categories = category_1)  
        else:
         return Product.get_all()  
    