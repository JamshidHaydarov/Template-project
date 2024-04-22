from django.contrib import admin
from .models import Admin, Product, Cart


@admin.register(Admin, Product, Cart)
class PersonAdmin(admin.ModelAdmin):
    pass

    # Register your models here.
