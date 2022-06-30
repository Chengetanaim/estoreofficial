from django.shortcuts import render
from store_information.models import ItemEstore, Item, EStore, HotDeals
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def men_collection(request):
    men_collection = ItemEstore.objects.filter(category='1')
    context = {'men_collection': men_collection}
    return render(request, 'estore_estore_sort/men_collection.html', context)


@login_required()
def ladies_collection(request):
    ladies_collection = ItemEstore.objects.filter(category='2')
    context = {'ladies_collection': ladies_collection}
    return render(request, 'estore_estore_sort/ladies_collection.html', context)


@login_required()
def kids_collection(request):
    kids_collection = ItemEstore.objects.filter(category='3')
    context = {'kids_collection': kids_collection}
    return render(request, 'estore_estore_sort/kids_collection.html', context)


@login_required()
def phones_tablets(request):
    phones_tablets = ItemEstore.objects.filter(category='4')
    context = {'phones_tablets': phones_tablets}
    return render(request, 'estore_estore_sort/phones_tablets.html', context)


@login_required()
def laptops(request):
    laptops = ItemEstore.objects.filter(category='5')
    context = {'laptops': laptops}
    return render(request, 'estore_estore_sort/laptops.html', context)


@login_required()
def appliances_machinery(request):
    appliances_machinery = ItemEstore.objects.filter(category='6')
    context = {'appliances_machinery': appliances_machinery}
    return render(request, 'estore_estore_sort/appliances_machinery.html', context)


@login_required()
def accessories(request):
    accessories = ItemEstore.objects.filter(category='7')
    context = {'accessories': accessories}
    return render(request, 'estore_estore_sort/accessories.html', context)


@login_required()
def dining_lounge(request):
    dining_lounge = ItemEstore.objects.filter(category='8')
    context = {'dining_lounge': dining_lounge}
    return render(request, 'estore_estore_sort/dining_lounge.html', context)


@login_required()
def kitchen(request):
    kitchen = ItemEstore.objects.filter(category='9')
    context = {'kitchen': kitchen}
    return render(request, 'estore_estore_sort/kitchen.html', context)


@login_required()
def bedroom(request):
    bedroom = ItemEstore.objects.filter(category='10')
    context = {'bedroom': bedroom}
    return render(request, 'estore_estore_sort/bedroom.html', context)


@login_required()
def bathroom(request):
    bathroom = ItemEstore.objects.filter(category='11')
    context = {'bathroom': bathroom}
    return render(request, 'estore_estore_sort/bathroom.html', context)


@login_required()
def skin_care(request):
    skin_care = ItemEstore.objects.filter(category='12')
    context = {'skin_care': skin_care}
    return render(request, 'estore_estore_sort/skin_care.html', context)


@login_required()
def hair_products(request):
    hair_products = ItemEstore.objects.filter(category='13')
    context = {'hair_products': hair_products}
    return render(request, 'estore_estore_sort/hair_products.html', context)


@login_required()
def fragrances(request):
    fragrances = ItemEstore.objects.filter(category='14')
    context = {'fragrances': fragrances}
    return render(request, 'estore_estore_sort/fragrances.html', context)


@login_required()
def cars(request):
    cars = ItemEstore.objects.filter(category='15')
    context = {'cars': cars}
    return render(request, 'estore_estore_sort/cars.html', context)


@login_required()
def trucks(request):
    trucks = ItemEstore.objects.filter(category='16')
    context = {'trucks': trucks}
    return render(request, 'estore_estore_sort/trucks.html', context)


@login_required()
def vehicle_parts(request):
    vehicle_parts = ItemEstore.objects.filter(category='17')
    context = {'vehicle_parts': vehicle_parts}
    return render(request, 'estore_estore_sort/vehicle_parts.html', context)


@login_required()
def event_services(request):
    event_services = ItemEstore.objects.filter(category='18')
    context = {'event_services': event_services}
    return render(request, 'estore_estore_sort/event_services.html', context)


@login_required()
def food_services(request):
    food_services = ItemEstore.objects.filter(category='19')
    context = {'food_services': food_services}
    return render(request, 'estore_estore_sort/food_services.html', context)


@login_required()
def other_services(request):
    other_services = ItemEstore.objects.filter(category='20')
    context = {'other_services': other_services}
    return render(request, 'estore_estore_sort/other_services.html', context)


@login_required()
def other(request):
    other = ItemEstore.objects.filter(category='21')
    context = {'other': other}
    return render(request, 'estore_estore_sort/other.html', context)

# Create your views here.
