from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect, HttpResponse
from .models import Product,Cart,ProductInCart
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    products = Product.objects.all()    
    # print(products)
    params = {'product': products}
    return render(request,'products/index.html',params)

@login_required
def addToCart(request,id):
    try:
        cart = Cart.objects.get(user=request.user)
        try:
            product=Product.objects.get(id = id)
            try:
                productincart = ProductInCart.objects.get(cart=cart,product=product)
                productincart.quantity = productincart.quantity + 1
                productincart.save()
                return redirect('displaycart')
            except:
                productincart = ProductInCart.objects.create(cart=cart,product=product,quantity=1)
                return redirect('displaycart')
        except:
            return redirect('')
    except:
        cart= Cart.objects.create(user=request.user)
        try:
            product = Product.objects.get(id =id)
            productincart = ProductInCart.objects.create(cart=cart, product=product, quantity=1)
            return redirect('displaycart')
        except:
            return redirect('displaycart')

def displaycart(request):

    try:
        queryset = ProductInCart.objects.filter(cart = request.user.cart)
        return render(request,'products/displaycart.html',{"cart":queryset})
    except:    
        return render(request,'products/displaycart.html')  


# class DisplayCart(LoginRequiredMixin, ListView):
#     model = ProductInCart
#     template_name = 'products/displaycart.html'
#     context_object_name ='cart'

#     def get_queryset(self):
#         queryset = ProductInCart.objects.filter(cart= self.request.user.cart)
#         return queryset

def viewproduct(request,id):

    viewproduct=Product.objects.get(id = id)
    return render(request,'products/viewproduct.html',{"product":viewproduct})
    
def deletefromcart(request,id):

    ProductInCart.objects.get(product_id=id).delete()
    return redirect('displaycart')
