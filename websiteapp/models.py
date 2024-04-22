from django.db import models


GENDER =[
    ('male', 'Male'),
    ('female', 'Female'),
]

class Admin(models.Model):
    user = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=35)
    gender = models.CharField(max_length=20, choices=GENDER)
    password = models.IntegerField()

    def __str__(self):
        return self.user

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to = 'images/')
    number = models.IntegerField(default=1)
    # name = models.CharField(max_length=20, db_index=True, verbose_name='Name')
    # slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Link')
    # price = models.CharField(max_length=5, decimal_places=2, verbose_name='Price')
    # description = models.CharField(max_length=1000, blank=True, verbose_name='Description')
    # avaible = models.BooleanField(default=True, verbose_name='Avaible')
    # created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    # uploaded = models.DateTimeField(auto_now=True, verbose_name='Uploaded')
    # image = models.ImageField(upload_to='images/', blank=True)


class Cart(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    number = models.IntegerField()
    image = models.ImageField(upload_to='cart_images/')
    description = models.CharField(max_length=100)
    total_of_product = models.IntegerField()
    total = models.IntegerField(default=1)
    pub_date = models.DateTimeField(auto_now=True)

class SendEmail(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=100)



    # class Meta:
    #     ordering = ('name')
    #     verbose_name ='Product'
    #     verbose_name_plural = "Product's"
    #     index_together = (('id', 'slug'), )


    def __str__(self):
        return self.name



# Create your models here.
