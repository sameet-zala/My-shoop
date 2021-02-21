from django.db import models

# Create your models here.
class Product(models.Model):

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "product/images")
    price = models.IntegerField()

    def __str__(self):
        return self.product_name
