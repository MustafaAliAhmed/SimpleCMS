from django.contrib import admin
from django.urls import  path

from . import views

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('homePage/', views.ShowAllProducts, name='showProducts'),
    path('product/<int:pk>/', views.productDetail, name='product'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='updateProduct'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='deleteProduct'),
    path('search/', views.searchBar, name='search'),
   
    
   
]
