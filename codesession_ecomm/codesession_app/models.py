from django.db import models

# Create your models here.


class ProductType(models.Model):
    Product_type = models.CharField(max_length=50)

    def __str__(self):
        return self.Product_type


class Product(models.Model):
    Product_Name = models.CharField(
        max_length=100, blank=False, verbose_name="Product Name")
    Product_Type = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    Product_Price = models.CharField(max_length=10, blank=False, null=False)
    Product_image = models.ImageField()
    Product_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Product_Name
