from django.contrib import admin
from .models import Item, EStore, ItemEstore, HotDeals, WishList

# Register your models here.
admin.site.register(Item)
admin.site.register(EStore)
admin.site.register(ItemEstore)
admin.site.register(HotDeals)
admin.site.register(WishList)