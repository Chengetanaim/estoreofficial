from django.contrib.auth.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'store_information'

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', views.items, name='gallery'),
    path('sell_product/', views.upload_item, name='sell_product'),
    path('create_estore/', views.create_estore, name='create_estore'),
    path('item_estore/', views.item_estore, name='item_estore'),
    path('welcome/', views.welcome, name='welcome'),
    path('about_estore/', views.about_estore, name='about_estore'),
    path('about_us/', views.about_us, name='about_us'),
    path('gallery/<int:gallerie_id>/', views.gallerie, name='gallerie'),
    path('estores/', views.estores, name='estores'),
    path('hotdeals/', views.hotdeals, name='hotdeals'),
    path('upload_hot_deals/', views.upload_hot_deals, name='upload_hot_deals'),
    path('hotdeals/<int:hotdeal_id>/', views.hotdeal, name='hotdeal'),
    path('estores_estore/<int:estore_id>/', views.estores_estore, name='estores_estore'),
    path('product_estore/<int:product_estore_id>/', views.product_estore, name='product_estore'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('my_listings/', views.my_listings, name='my_listings'),
    path('my_gallery/', views.my_gallery, name='my_gallery'),
    path('estore_coupon/', views.estore_coupon, name='estore_coupon'),
    path('create/', views.create, name='create'),
    path('no_store', views.no_store, name='no_store'),
    path('edit_store/<int:estore_id>/', views.edit_store, name='edit_store'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
