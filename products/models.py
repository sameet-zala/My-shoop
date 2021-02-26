from django.db import models
from accounts.models import CustomUser
from datetime import timezone
# Create your models here.
class Product(models.Model):

    # product_id = models.AutoField(null=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to = "product/images")
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

class Cart(models.Model):
    
    cart_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(CustomUser, on_delete= models.CASCADE)
    # created_on = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.first_name

class ProductInCart(models.Model):
  
    class Meta:
        unique_together = (('cart','product'),)
    product_in_cart_id = models.AutoField(primary_key=True)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        return self.product.product_name

