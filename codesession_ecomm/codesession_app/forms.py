from .models import Product
from django import forms


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['Product_Name', 'Product_Type',
                  'Product_Price', 'Product_image']
