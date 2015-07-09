from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.TextField()

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name
