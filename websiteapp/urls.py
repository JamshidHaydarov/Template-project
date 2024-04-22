from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name='about'),
    path('single-product/<int:id>/', views.single_product, name='single-product'),
    path('dangasalik/', views.secret_method),
    path('more-info/', views.more_info,),
    path('update/<int:id>/', views.update),
    path('cart/', views.cart, name='cart'),
    path('product-list/', views.product_list, name='product-list'),
    path('product-update/<int:id>/', views.product_update, name='product-update'),
    path('product-delete/<int:id>/', views.product_delete, name='product-delete'),
    path('product-create/', views.ProductUpdate.as_view(), name='product-create'),
    path('send-email', views.send_email, name='send-email'),
    path('contact', views.contact, name='contact'),
]
