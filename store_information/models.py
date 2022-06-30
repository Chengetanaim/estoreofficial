from django.db import models
from account.models import Account

# Create your models here.


class Item(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    category = models.CharField(max_length=100)
    image1 = models.ImageField(models.ImageField(upload_to='images/'))
    image2 = models.ImageField(models.ImageField(upload_to='images/'))
    image3 = models.ImageField(models.ImageField(upload_to='images/'))
    image4 = models.ImageField(models.ImageField(upload_to='images/'))
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + ' - ' + self.price


class EStore(models.Model):
    store_name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profile_pic = models.ImageField(models.ImageField(upload_to='images/'))
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.store_name


class ItemEstore(models.Model):
    estore = models.ForeignKey(EStore, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    category = models.CharField(max_length=100)
    image1 = models.ImageField(models.ImageField(upload_to='images/'))
    image2 = models.ImageField(models.ImageField(upload_to='images/'))
    image3 = models.ImageField(models.ImageField(upload_to='images/'))
    image4 = models.ImageField(models.ImageField(upload_to='images/'))
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name


class HotDeals(models.Model):
    image = models.ImageField(models.ImageField(upload_to='images/'))
    description = models.TextField(max_length=200)
    category = models.CharField(max_length=100, default="None")
    owner = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description


class WishList(models.Model):
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    owner = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='my_wishlist') # Name should be wishlist and do reverse thingy lol

    def __str__(self):
        return str(self.product)












