from django.urls import path, include
from . import views

app_name = 'estore_estore_sort'
urlpatterns = [
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
    path('other/', views.other, name='other'),

]