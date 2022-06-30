from django.urls import path, include
from . import views

app_name = 'sort'
urlpatterns = [
    path('clothing/', views.clothing, name='clothing'),
    path('electronics/', views.electronics, name='electronics'),
    path('homeware/', views.homeware, name='homeware'),
    path('other/', views.other, name='other'),
    path('clothing_estore/', views.clothing_estore, name='clothing_estore'),
    path('electronics_estore/', views.electronics_estore, name='electronics_estore'),
    path('homeware_estore/', views.homeware_estore, name='homeware_estore'),
    path('other_estore/', views.other_estore, name='other_estore'),
    path('cosmetics_estore/', views.cosmetics_estore, name='cosmetics_estore'),
    path('vehicles_estore/', views.vehicles_estore, name='vehicles_estore'),
    path('men_collection/', views.men_collection, name='men_collection'),
    path('ladies_collection/', views.ladies_collection, name='ladies_collection'),
    path('kids_collection/', views.kids_collection, name='kids_collection'),
    path('phones_tablets/', views.phones_tablets, name='phones_tablets'),
    path('laptops/', views.laptops, name='laptops'),
    path('appliances_machinery/', views.appliances_machinery, name='appliances_machinery'),
    path('accessories/', views.accessories, name='accessories'),
    path('dining_lounge/', views.dining_lounge, name='dining_lounge'),
    path('kitchen/', views.kitchen, name='kitchen'),
    path('bedroom/', views.bedroom, name='bedroom'),
    path('bathroom/', views.bathroom, name='bathroom'),
    path('skin_care/', views.skin_care, name='skin_care'),
    path('hair_products/', views.hair_products, name='hair_products'),
    path('fragrances/', views.fragrances, name='fragrances'),
    path('cars/', views.cars, name='cars'),
    path('trucks/', views.trucks, name='trucks'),
    path('vehicle_parts/', views.vehicle_parts, name='vehicle_parts'),
    path('event_services/', views.event_services, name='event_services'),
    path('food_services/', views.food_services, name='food_services'),
    path('other_services/', views.other_services, name='other_services'),
    path('other_electronics/', views.other_electronics, name='other_electronics'),
    path('other_beauty_cosmetics/', views.other_beauty_cosmetics, name='other_beauty_cosmetics'),
    path('other_vehicles/', views.other_vehicles, name='other_vehicles'),
    path('other_homeware/', views.other_homeware, name='other_homeware'),


]