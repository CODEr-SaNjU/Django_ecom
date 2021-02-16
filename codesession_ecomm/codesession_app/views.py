from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from .models import Product, ProductType
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, auth, Group
# Create your views here.


@login_required(login_url='login')
def Dashboard(request):
    return render(request, "Admin_html/main.htm")


def HomePage(request):
    AllProduct = Product.objects.all()
    return render(request, "custmer_html/main.htm", {'AllProduct': AllProduct})


def Login(request):
    if request.method == "POST":
        Username = request.POST["UserName"]
        Password = request.POST["Password"]
        user = auth.authenticate(username=Username, password=Password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')

        else:
            return render(request, 'Admin_html/login.htm')

    else:
        return render(request, 'Admin_html/login.htm')


def Add_Product(request):
    return render(request, 'Admin_html/Add_product.htm')


def Add_ProductType(request):
    if request.method == "POST":
        AddProductType = request.POST["productType"]

        if ProductType.objects.filter(Product_type=AddProductType).exists():
            return HttpResponse("data exists ")
        else:
            Productype = ProductType.objects.create(
                Product_type=AddProductType)
            Productype.save()
            return HttpResponse("data done ")
    else:
        return render(request, 'Admin_html/product_type.htm')
