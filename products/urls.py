from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='index'),
    path('addtocart/<int:id>/', views.addToCart,name='addtocart'),
    path('displaycart/', views.displaycart,name='displaycart'),
    path('deletefromcart/<int:id>/', views.deletefromcart,name='deletefromcart'),
    path('viewproduct/<int:id>/', views.viewproduct,name='viewproduct'),

]