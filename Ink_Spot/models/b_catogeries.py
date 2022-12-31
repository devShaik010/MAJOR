from django.db import models

class B_categories(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def all_catogaries():
        return B_categories.objects.all()    