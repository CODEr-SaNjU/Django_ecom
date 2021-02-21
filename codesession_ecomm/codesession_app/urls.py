from django.urls import path, include
from . import views

urlpatterns = [
    path('Dashboard/', views.Dashboard, name="dashboard"),
    path('', views.HomePage, name="homepage"),
    path('Login/', views.Login, name="login"),
    path('AddProduct/', views.Add_Product, name='AddProduct'),
    path('AddProductType/', views.Add_ProductType, name="AddProductType"),
    path('UpdateProduct/<int:id>/Update/',
         views.Update_Product, name="UpdateProduct"),
    path('DeleteProduct/<int:id>/Delete/',
         views.Delete_Product, name="DeleteProduct")
]
