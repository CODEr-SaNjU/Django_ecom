from django.urls import path, include
from . import views

urlpatterns = [
    path('Dashboard/', views.Dashboard, name="dashboard"),
    path('', views.HomePage, name="homepage"),
    path('Login/', views.Login, name="login"),
    path('AddProduct/', views.Add_Product, name='AddProduct'),
    path('AddProductType/', views.Add_ProductType, name="AddProductType"),
]
