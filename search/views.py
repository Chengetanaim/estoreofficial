from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from store_information.models import Item, EStore, ItemEstore, HotDeals
from .models import Coupon
from django.contrib.auth.decorators import login_required


class SearchResultsView(ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(
        Q(product_name__icontains=query) | Q(location__icontains=query)
        )
        return object_list


class StoreSearchResultsView(ListView):
    model = EStore
    template_name = 'store_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = EStore.objects.filter(
        Q(store_name__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query)
        )
        return object_list


class ProductStoreSearchResultsView(ListView):
    model = ItemEstore
    template_name = 'product_store_search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =  ItemEstore.objects.filter(
        Q(product_name__icontains=query) | Q(category__icontains=query)
        )
        return object_list


class SearchMobileResultsView(ListView):
    model = Item
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Item.objects.filter(
        Q(product_name__icontains=query) | Q(location__icontains=query)
        )
        return object_list


def mobile(request):
    return render(request, 'mobile.html')


def estore_mobile(request):
    return render(request, 'estore_mobile.html')


class EstoreMobileResultsView(ListView):
    model = EStore
    template_name = 'estore_mobile_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = EStore.objects.filter(
        Q(store_name__icontains=query) | Q(location__icontains=query) | Q(category__icontains=query)
        )
        return object_list


class EstoreCouponResultsView(ListView):
    model = Coupon
    template_name = 'store_information/create.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Coupon.objects.filter(
            Q(name__exact=query)
        )
        return object_list


class GalleryCouponResultsView(ListView):
    model = Coupon
    template_name = 'store_information/sell_product.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Coupon.objects.filter(
        Q(name__exact=query)
        )
        return object_list


class HotDealsCouponResultsView(ListView):
    model = Coupon
    template_name = 'store_information/upload_hot_deals.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Coupon.objects.filter(
        Q(name__exact=query)
        )
        return object_list