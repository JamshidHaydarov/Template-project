from django.forms import ModelForm
from .models import Product, SendEmail

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['number']

class AdminProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description','price', 'image', 'number']

class SendEmailForm(ModelForm):
    class Meta:
        model = SendEmail
        fields =['name', 'email']