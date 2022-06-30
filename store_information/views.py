from django.shortcuts import render, redirect
from .models import Item, ItemEstore, HotDeals, WishList
from .forms import ItemForm, Create_EStoreForm, ItemEstoreForm, EStore, HotDealsForm
from account.models import Account
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json
# Create your views here.


@login_required()
def index(request):
    items2 = Item.objects.filter(location='Harare').order_by('-date_added')
    hotdeals = HotDeals.objects.order_by('-date_added')
    context = {'items2': items2, 'hot_deals': hotdeals}
    return render(request, 'store_information/index.html', context)


def items(request):
    items = Item.objects.order_by('-date_added')
    context = {'items': items}
    return render(request, 'store_information/gallery.html', context)


@login_required()
def upload_item(request):
    if request.method != 'POST':
        form = ItemForm()
    else:
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.owner = request.user
            new_item.save()
            data = form.cleaned_data.get("price")
            if data >= '0':
                return redirect('store_information:hotdeals')
    context = {'form': form}
    return render(request, 'store_information/sell_product.html', context)

@login_required()
def create_estore(request):
    if request.method != 'POST':
        form = Create_EStoreForm()
    else:
        form = Create_EStoreForm(request.POST, request.FILES)
        if form.is_valid():
            new_estore = form.save(commit=False)
            new_estore.owner = request.user
            new_estore.save()
            return redirect('store_information:about_estore')
    context = {'form': form}
    return render(request, 'store_information/create_estore.html', context)



@login_required()
def item_estore(request):
    if request.method != 'POST':
        form = ItemEstoreForm()
    else:
        form = ItemEstoreForm(request.POST, request.FILES)
        if form.is_valid():

            new_itemestore = form.save(commit=False)
            new_itemestore.owner = request.user
            new_itemestore.save()
            return redirect('store_information:about_estore')
    context = {'form': form}
    return render(request, 'store_information/item_estore.html', context)


def welcome(request):
    return render(request, 'store_information/welcome.html')


@login_required()
def about_estore(request):
    abouts = EStore.objects.filter(owner=request.user)
    context = {'abouts': abouts}
    return render(request, 'store_information/about_estore.html', context)


def about_us(request):
    return render(request, 'store_information/about_us.html')


@login_required()
def gallerie(request, gallerie_id):
    wishes = []
    gallerie = Item.objects.get(id=gallerie_id)
    estores = gallerie.owner.estore_set.order_by('-date_added')
    items2 = Item.objects.filter(location=request.user.location)
    user = request.user
    wishlist = user.my_wishlist.all()
    for wish in wishlist:
        wishes.append(wish.product)
    context = {'gallerie': gallerie, 'items2': items2, 'user': user, 'wishes': wishes, 'estores': estores}
    return render(request, 'store_information/gallerie.html', context)


@login_required()
def estores(request):
    estores = EStore.objects.order_by('-date_added')
    context = {'estores': estores}
    return render(request, 'store_information/estores.html', context)


@login_required()
def hotdeals(request):
    hotdeals = HotDeals.objects.order_by('-date_added')
    context = {'hotdeals': hotdeals}
    return render(request, 'store_information/hotdeals.html', context)


@login_required()
def upload_hot_deals(request):
    if request.method != 'POST':
        form = HotDealsForm()
    else:
        form = HotDealsForm(request.POST, request.FILES)
        if form.is_valid():
            new_hot_deal = form.save(commit=False)
            new_hot_deal.owner = request.user
            new_hot_deal.save()
            return redirect('store_information:hotdeals')
    context = {'form': form}
    return render(request, 'store_information/upload_hot_deals.html', context)


@login_required()
def hotdeal(request, hotdeal_id):
    hotdeal = HotDeals.objects.get(id=hotdeal_id)
    estores = hotdeal.owner.estore_set.order_by('-date_added')
    context = {'hotdeal': hotdeal, 'estores': estores}
    return render(request, 'store_information/hot_deal.html', context)


@login_required()
def estores_estore(request, estore_id):
    estores_estore = EStore.objects.get(id=estore_id)
    items = estores_estore.itemestore_set.order_by('-date_added')
    context = {'estores_estore': estores_estore, 'items': items}
    return render(request, 'store_information/estores_estore.html', context)


@login_required()
def product_estore(request, product_estore_id):
    product_estore = ItemEstore.objects.get(id=product_estore_id)
    estores = product_estore.owner.estore_set.order_by('-date_added')
    context = {'product_estore': product_estore, 'estores': estores}
    return render(request, 'store_information/product_estore.html', context)

@login_required()
def wishlist(request):
    user = request.user
    wishlist = user.my_wishlist.all()
    context = {'wishlist': wishlist}
    print(wishlist)
    for wish in wishlist:
        print(wish.product)
    return render(request, 'store_information/wishlist.html', context)


@login_required()
def add_to_wishlist(request):
    data = json.loads(request.body)
    item_id = data['item_id']
    action = data['action']

    print(item_id, action)

    if item_id and action:
        try:
            item = Item.objects.get(id=item_id)
            if action == 'add':
                WishList.objects.get_or_create(product=item, owner=request.user)
                
            else:
                WishList.objects.filter(product=item, owner=request.user).delete()
            return JsonResponse({'status': 'ok'})

        except Item.DoesNotExist:
            return JsonResponse({'status': 'error'})

    return JsonResponse({'status': 'error'})


@login_required()
def my_listings(request):
    items = Item.objects.filter(owner=request.user)
    context = {'items': items}
    return render(request, 'store_information/my_listings.html', context)


def my_gallery(request):
    return render(request, 'store_information/final draft/myGallery.html')

@login_required()
def estore_coupon(request):
    return render(request, 'store_information/estore_coupon.html')

@login_required()
def create(request):
    return render(request, 'store_information/create.html')


@login_required()
def no_store(request):
    return render(request, 'store_information/no_store.html')


@login_required()
def edit_store(request, estore_id):
    estore = EStore.objects.get(id=estore_id)
    if request.method != 'POST':
        form = Create_EStoreForm(instance=estore)
    else:
        form = Create_EStoreForm(request.POST, request.FILES, instance=estore)
        if form.is_valid():
            form.save()
            return redirect('store_information:about_estore')
    context = {'estore': estore, 'form': form}
    return render(request, 'store_information/edit_store.html', context)


def terms_conditions(request):
    return render(request, 'store_information/terms_conditions.html')















