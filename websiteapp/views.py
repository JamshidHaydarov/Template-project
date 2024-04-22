from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.forms import ModelForm
from django.shortcuts import get_object_or_404
from .form import ProductForm, AdminProductForm, SendEmailForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    product = Product.objects.all()
    print(product)
    # for i in product:
    #     print(i.price)
    return render(request, "index.html", context={"context" : product})


def contact(request):
    return render(request, "contact.html", context={})


def single_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, "single-product.html", context={"context": product})

def about(request):
    return render(request, 'about.html', context={})



def more_info(request):
    return render(request, 'more-info.html', context={})

def cart(request):
    cart = Cart.objects.all()
    result = 0
    for i in cart:
        result = i.total
    return render(request, 'cart.html', context={"context": cart, "cart" : str(result)})

def update(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance = product)
    if form.is_valid():
        form.save()
        cart = Cart.objects.all()
        res = product.price * product.number
        for i in cart:
            res += i.total_of_product
        # print(res)
        a = Cart(name = product.name, price = product.price, number = product.number, image = product.image, description = product.description, total_of_product =  product.number * product.price, total=res)
        a.save()
        return redirect('index')
    return render(request, 'update.html', context={'context': form, "product": product})


def product_update(request, id):
    product = get_object_or_404(Product, id=id)
    form = AdminProductForm(request.POST or None, instance= product)
    if form.is_valid():
        form.save()
        return redirect('product-list')

    return render(request, 'product-update.html', context={"form" : form})



def product_delete(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('product-list')


# def product_create(request):
#     if request.method == 'POST':
#         form = AdminProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # model = form.instance
#             return redirect('product-list')
#     else:
#         form = AdminProductForm()

#     return render(request, 'product-create.html', context={'form': form})

class ProductUpdate(CreateView):
    model = Product
    class_form = AdminProductForm
    template_name = 'product-create.html'
    fields = ['name', 'description', 'price', 'image', 'number']
    success_url = reverse_lazy('product-list')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product-list.html', context={'products': products})


def send_email(request):
    if request.method == 'POST':
        form = SendEmailForm(request.POST)
        if form.is_valid():
            form.save()
            sendmail = SendEmail.objects.all()
            res = ''
            for i in sendmail:
                res = i.email
            subject = "it's send email function"
            message = 'Hexa Shop Administration'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [res]
            send_mail(subject, message, email_from, recipient_list)
            # model = form.instance
            return redirect('index')
    else:
        form = SendEmailForm()

    return render(request, 'contact.html', context={'forms': form})











def secret_method(request):
    return HttpResponse("Saytni bu yerini chopib tashlaganim uchun bu viewni yozib otirmadim)")