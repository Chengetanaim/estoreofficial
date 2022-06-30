from django.shortcuts import render
from store_information.models import ItemEstore, Item, EStore, HotDeals
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required()
def clothing(request):
    clothing = Item.objects.filter(category='Clothing')
    clothing_estore = EStore.objects.filter(category='Clothing')
    context = {'clothing': clothing, 'clothing_estore': clothing_estore}
    return render(request, 'sorting/clothing.html', context)


@login_required()
def electronics(request):
    electronics = Item.objects.filter(category='Electronics')
    electronics_estore = EStore.objects.filter(category='Electronics')
    context = {'electronics': electronics, 'electronics_estore': electronics_estore}
    return render(request, 'sorting/electronics.html', context)


@login_required()
def homeware(request):
    homeware = Item.objects.filter(category='Homeware')
    homeware_estore = EStore.objects.filter(category='Homeware')
    context = {'homeware': homeware, 'homeware_estore': homeware_estore}
    return render(request, 'sorting/homeware.html', context)


@login_required()
def other(request):
    other = Item.objects.filter(category='Other')
    other_estore = EStore.objects.filter(category='Other')
    context = {'other': other, 'other_estore': other_estore}
    return render(request, 'sorting/other.html', context)


@login_required()
def clothing_estore(request):
    clothing_estore = EStore.objects.filter(category='Clothing')
    context = {'clothing_estore': clothing_estore}
    return render(request, 'sorting/clothing_estore.html', context)


@login_required()
def electronics_estore(request):
    electronics_estore = EStore.objects.filter(category='Electronics')
    context = {'electronics_estore': electronics_estore}
    return render(request, 'sorting/electronics_estore.html', context)


@login_required()
def homeware_estore(request):
    homeware_estore = EStore.objects.filter(category='Homeware')
    context = {'homeware_estore': homeware_estore}
    return render(request, 'sorting/homeware_estore.html', context)


@login_required()
def other_estore(request):
    other_estore = EStore.objects.filter(category='Other')
    context = {'other_estore': other_estore}
    return render(request, 'sorting/other_estore.html', context)


@login_required()
def cosmetics_estore(request):
    cosmetics_estore = EStore.objects.filter(category='1')
    context = {'cosmetics_estore': cosmetics_estore}
    return render(request, 'sorting/cosmetics_estore.html', context)


@login_required()
def vehicles_estore(request):
    vehicles_estore = EStore.objects.filter(category='Vehicles')
    context = {'vehicles_estore': vehicles_estore}
    return render(request, 'sorting/vehicles_estore.html', context)


@login_required()
def men_collection(request):
    men_collection = Item.objects.filter(category='1')
    context = {'men_collection': men_collection}
    return render(request, 'sorting/men_collection.html', context)


@login_required()
def ladies_collection(request):
    ladies_collection = Item.objects.filter(category='2')
    context = {'ladies_collection': ladies_collection}
    return render(request, 'sorting/ladies_collection.html', context)


@login_required()
def kids_collection(request):
    kids_collection = Item.objects.filter(category='3')
    context = {'kids_collection': kids_collection}
    return render(request, 'sorting/kids_collection.html', context)


@login_required()
def phones_tablets(request):
    phones_tablets = Item.objects.filter(category='4')
    context = {'phones_tablets': phones_tablets}
    return render(request, 'sorting/phones_tablets.html', context)


@login_required()
def laptops(request):
    laptops = Item.objects.filter(category='5')
    context = {'laptops': laptops}
    return render(request, 'sorting/laptops.html', context)


@login_required()
def appliances_machinery(request):
    appliances_machinery = Item.objects.filter(category='6')
    context = {'appliances_machinery': appliances_machinery}
    return render(request, 'sorting/appliances_machinery.html', context)


@login_required()
def accessories(request):
    accessories = Item.objects.filter(category='7')
    context = {'accessories': accessories}
    return render(request, 'sorting/accessories.html', context)


@login_required()
def dining_lounge(request):
    dining_lounge = Item.objects.filter(category='8')
    context = {'dining_lounge': dining_lounge}
    return render(request, 'sorting/dining_lounge.html', context)


@login_required()
def kitchen(request):
    kitchen = Item.objects.filter(category='9')
    context = {'kitchen': kitchen}
    return render(request, 'sorting/kitchen.html', context)


@login_required()
def bedroom(request):
    bedroom = Item.objects.filter(category='10')
    context = {'bedroom': bedroom}
    return render(request, 'sorting/bedroom.html', context)


@login_required()
def bathroom(request):
    bathroom = Item.objects.filter(category='11')
    context = {'bathroom': bathroom}
    return render(request, 'sorting/bathroom.html', context)


@login_required()
def skin_care(request):
    skin_care = Item.objects.filter(category='12')
    context = {'skin_care': skin_care}
    return render(request, 'sorting/skin_care.html', context)


@login_required()
def hair_products(request):
    hair_products = Item.objects.filter(category='13')
    context = {'hair_products': hair_products}
    return render(request, 'sorting/hair_products.html', context)


@login_required()
def fragrances(request):
    fragrances = Item.objects.filter(category='14')
    context = {'fragrances': fragrances}
    return render(request, 'sorting/fragrances.html', context)


@login_required()
def cars(request):
    cars = Item.objects.filter(category='15')
    context = {'cars': cars}
    return render(request, 'sorting/cars.html', context)


@login_required()
def trucks(request):
    trucks = Item.objects.filter(category='16')
    context = {'trucks': trucks}
    return render(request, 'sorting/trucks.html', context)


@login_required()
def vehicle_parts(request):
    vehicle_parts = Item.objects.filter(category='17')
    context = {'vehicle_parts': vehicle_parts}
    return render(request, 'sorting/vehicle_parts.html', context)


@login_required()
def event_services(request):
    event_services = Item.objects.filter(category='18')
    context = {'event_services': event_services}
    return render(request, 'sorting/event_services.html', context)


@login_required()
def food_services(request):
    food_services = Item.objects.filter(category='19')
    context = {'food_services': food_services}
    return render(request, 'sorting/food_services.html', context)


@login_required()
def other_services(request):
    other_services = Item.objects.filter(category='20')
    context = {'other_services': other_services}
    return render(request, 'sorting/other_services.html', context)


@login_required()
def other(request):
    other = Item.objects.filter(category='21')
    context = {'other': other}
    return render(request, 'sorting/other.html', context)


@login_required()
def other_electronics(request):
    other_electronics = Item.objects.filter(category='22')
    context = {'other_electronics': other_electronics}
    return render(request, 'sorting/other_electronics.html', context)


@login_required()
def other_beauty_cosmetics(request):
    other_beauty_cosmetics = Item.objects.filter(category='23')
    context = {'other_beauty_cosmetics': other_beauty_cosmetics}
    return render(request, 'sorting/other_beauty_cosmetics.html', context)

@login_required()
def other_vehicles(request):
    other_vehicles = Item.objects.filter(category='24')
    context = {'other_vehicles': other_vehicles}
    return render(request, 'sorting/other_vehicles.html', context)


@login_required()
def other_homeware(request):
    other_homeware = Item.objects.filter(category='25')
    context = {'other_homeware': other_homeware}
    return render(request, 'sorting/other_homeware.html', context)



