from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import auth, messages
from .models import Product, ProductType
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, auth, Group
from .forms import ProductCreateForm


@login_required(login_url='login')
def Dashboard(request):
    AllProduct = Product.objects.all()
    return render(request, "Admin_html/main.htm", {'AllProduct': AllProduct})


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
    if request.method == "POST":
        Productform = ProductCreateForm(request.POST, request.FILES)
        if Productform.is_valid():
            product = Productform.save(commit=False)
            product.save()
            return redirect('dashboard')
        Productform = ProductCreateForm()
        return render(request, 'Admin_html/Add_product.htm', {'form': Productform})
    else:
        Productform = ProductCreateForm()
        return render(request, 'Admin_html/Add_product.htm', {'form': Productform})


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


def Update_Product(request, id):
    obj = get_object_or_404(Product, id=id)
    print("line number 70 ", id)
    form = ProductCreateForm(request.POST or None, request.FILES, instance=obj)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        form.save()
        return redirect('dashboard')
        Productform = ProductCreateForm()
        return render(request, 'Admin_html/Add_product.htm', {'form': Productform})
    else:
        Productform = ProductCreateForm()
        return render(request, 'Admin_html/Add_product.htm', {'form': Productform})


def Delete_Product(request, id):
    pass
