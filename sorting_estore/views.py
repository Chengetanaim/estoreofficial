from django.shortcuts import render
from store_information.models import ItemEstore, Item, EStore, HotDeals
from django.contrib.auth.decorators import login_required

# Create your views here


@login_required()
def men_collection(request):
    men_collection = EStore.objects.filter(category='men_collection')
    context = {'men_collection': men_collection}
    return render(request, 'sorting_estore/men_collection.html', context)


@login_required()
def ladies_collection(request):
    ladies_collection = EStore.objects.filter(category='ladies_collection')
    context = {'ladies_collection': ladies_collection}
    return render(request, 'sorting_estore/ladies_collection.html', context)


@login_required()
def kids_collection(request):
    kids_collection = EStore.objects.filter(category='kids_collection')
    context = {'kids_collection': kids_collection}
    return render(request, 'sorting_estore/kids_collection.html', context)


@login_required()
def phones_tablets(request):
    phones_tablets = EStore.objects.filter(category='phones_tablets')
    context = {'phones_tablets': phones_tablets}
    return render(request, 'sorting_estore/phones_tablets.html', context)


@login_required()
def laptops(request):
    laptops = EStore.objects.filter(category='laptops')
    context = {'laptops': laptops}
    return render(request, 'sorting_estore/laptops.html', context)


@login_required()
def appliances_machinery(request):
    appliances_machinery = EStore.objects.filter(category='appliances_machinery')
    context = {'appliances_machinery': appliances_machinery}
    return render(request, 'sorting_estore/appliances_machinery.html', context)


@login_required()
def accessories(request):
    accessories = EStore.objects.filter(category='accessories')
    context = {'accessories': accessories}
    return render(request, 'sorting_estore/accessories.html', context)


@login_required()
def dining_lounge(request):
    dining_lounge = EStore.objects.filter(category='dining_lounge')
    context = {'dining_lounge': dining_lounge}
    return render(request, 'sorting_estore/dining_lounge.html', context)


@login_required()
def kitchen(request):
    kitchen = EStore.objects.filter(category='kitchen')
    context = {'kitchen': kitchen}
    return render(request, 'sorting_estore/kitchen.html', context)


@login_required()
def bedroom(request):
    bedroom = EStore.objects.filter(category='bedroom')
    context = {'bedroom': bedroom}
    return render(request, 'sorting_estore/bedroom.html', context)


@login_required()
def bathroom(request):
    bathroom = EStore.objects.filter(category='bathroom')
    context = {'bathroom': bathroom}
    return render(request, 'sorting_estore/bathroom.html', context)


@login_required()
def skin_care(request):
    skin_care = EStore.objects.filter(category='skin_care')
    context = {'skin_care': skin_care}
    return render(request, 'sorting_estore/skin_care.html', context)


@login_required()
def hair_products(request):
    hair_products = EStore.objects.filter(category='hair_products')
    context = {'hair_products': hair_products}
    return render(request, 'sorting_estore/hair_products.html', context)


@login_required()
def fragrances(request):
    fragrances = EStore.objects.filter(category='fragrances')
    context = {'fragrances': fragrances}
    return render(request, 'sorting_estore/fragrances.html', context)


@login_required()
def cars(request):
    cars = EStore.objects.filter(category='cars')
    context = {'cars': cars}
    return render(request, 'sorting_estore/cars.html', context)


@login_required()
def trucks(request):
    trucks = EStore.objects.filter(category='trucks')
    context = {'trucks': trucks}
    return render(request, 'sorting_estore/trucks.html', context)


@login_required()
def vehicle_parts(request):
    vehicle_parts = EStore.objects.filter(category='vehicle_parts')
    context = {'vehicle_parts': vehicle_parts}
    return render(request, 'sorting_estore/vehicle_parts.html', context)


@login_required()
def event_services(request):
    event_services = EStore.objects.filter(category='event_services')
    context = {'event_services': event_services}
    return render(request, 'sorting_estore/event_services.html', context)


@login_required()
def food_services(request):
    food_services = EStore.objects.filter(category='food_services')
    context = {'food_services': food_services}
    return render(request, 'sorting_estore/food_services.html', context)


@login_required()
def other_services(request):
    other_services = EStore.objects.filter(category='other_services')
    context = {'other_services': other_services}
    return render(request, 'sorting_estore/other_services.html', context)


@login_required()
def other(request):
    other = EStore.objects.filter(category='other')
    context = {'other': other}
    return render(request, 'sorting_estore/other.html', context)


@login_required()
def men_collection_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='1')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/men_collection_hotdeals.html', context)


@login_required()
def ladies_collection_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='2')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/ladies_collection_hotdeals.html', context)


@login_required()
def kids_collection_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='3')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/kids_collection_hotdeals.html', context)


@login_required()
def phones_tablets_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='4')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/phones_tablets_hotdeals.html', context)


@login_required()
def laptops_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='5')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/laptops_hotdeals.html', context)


@login_required()
def appliances_machinery_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='6')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/appliances_machinery_hotdeals.html', context)


@login_required()
def accessories_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='7')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/accessories_hotdeals.html', context)


@login_required()
def dining_lounge_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='8')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/dining_lounge_hotdeals.html', context)


@login_required()
def kitchen_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='9')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/kitchen_hotdeals.html', context)


@login_required()
def bedroom_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='10')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/bedroom_hotdeals.html', context)


@login_required()
def bathroom_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='11')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/bathroom_hotdeals.html', context)


@login_required()
def skin_care_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='12')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/skin_care_hotdeals.html', context)


@login_required()
def hair_products_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='13')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/hair_products_hotdeals.html', context)


@login_required()
def fragrances_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='14')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/fragrances_hotdeals.html', context)


@login_required()
def cars_hotdeals(request):
    hotdeals = EStore.objects.filter(category='15')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/cars_hotdeals.html', context)


@login_required()
def trucks_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='16')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/trucks_hotdeals.html', context)


@login_required()
def vehicle_parts_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='17')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/vehicle_parts_hotdeals.html', context)


@login_required()
def event_services_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='18')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/event_services_hotdeals.html', context)


@login_required()
def food_services_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='19')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/food_services_hotdeals.html', context)


@login_required()
def other_services_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='20')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/other_services_hotdeals.html', context)


@login_required()
def other_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='21')
    context = {'hotdeals': hotdeals}


@login_required()
def other_electronics(request):
    other_electronics = EStore.objects.filter(category='other electronics')
    context = {'other_electronics': other_electronics}
    return render(request, 'sorting_estore/other_electronics.html', context)


@login_required()
def other_beauty_cosmetics(request):
    other_beauty_cosmetics = EStore.objects.filter(category='other beauty cosmetics')
    context = {'other_beauty_cosmetics': other_beauty_cosmetics}
    return render(request, 'sorting_estore/other_beauty_cosmetics.html', context)


@login_required()
def other_vehicles(request):
    other_vehicles = EStore.objects.filter(category='other vehicles')
    context = {'other_vehicles': other_vehicles}
    return render(request, 'sorting_estore/other_vehicles.html', context)


@login_required()
def other_homeware(request):
    other_homeware = EStore.objects.filter(category='other homeware')
    context = {'other_homeware': other_homeware}
    return render(request, 'sorting_estore/other_homeware.html', context)


@login_required()
def other_electronics_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='22')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/other_electronics_hotdeals.html', context)


@login_required()
def other_beauty_cosmetics_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='23')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/other_beauty_cosmetics_hotdeals.html', context)


@login_required()
def other_vehicles_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='24')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/other_vehicles_hotdeals.html', context)


@login_required()
def other_homeware_hotdeals(request):
    hotdeals = HotDeals.objects.filter(category='25')
    context = {'hotdeals': hotdeals}
    return render(request, 'sorting_estore/other_homeware_hotdeals.html', context)


