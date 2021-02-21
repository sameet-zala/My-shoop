from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):

    products = Product.objects.all()    
    print(products)
    params = {'product': products}
    return render(request,'products/index.html',params)