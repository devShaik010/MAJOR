from django.db import models
from .b_catogeries import B_categories

class Book(models.Model):
    name = models.CharField(max_length=40)
    a_uth = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    language = models.CharField(max_length=10)
    image = models.ImageField(upload_to="Uploads\Books")
    image_1 = models.ImageField(upload_to="Uploads\Books")
    image_2 = models.ImageField(upload_to="Uploads\Books")
    desc = models.CharField(max_length=500)
    b_categories = models.ForeignKey(B_categories,on_delete=models.CASCADE, default=1)

   #storing data in function 
    @staticmethod
    def get_all():
        return Book.objects.all()

    @staticmethod
    def get_all_filter(b_category):
        if b_category:
            return Book.objects.filter(b_categories = b_category )    