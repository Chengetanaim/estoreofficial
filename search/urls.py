from django.urls import path

from .views import SearchResultsView, StoreSearchResultsView, ProductStoreSearchResultsView, SearchMobileResultsView, EstoreMobileResultsView, EstoreCouponResultsView, GalleryCouponResultsView, HotDealsCouponResultsView
from . import views


urlpatterns = [
    path('result/', SearchResultsView.as_view(), name='search_results'),
    path('store_result/', StoreSearchResultsView.as_view(), name='store_search_results'),
    path('product_store_result/', ProductStoreSearchResultsView.as_view(), name='product_store_search_results'),
    path('search_mobile/', SearchMobileResultsView.as_view(), name='search_mobile_results'),
    path('mobile/', views.mobile, name='mobile'),
    path('estore_mobile/', views.estore_mobile, name='estore_mobile'),
    path('estore_mobile_results/', EstoreMobileResultsView.as_view(), name='estore_mobile_results'),
    path('estore_coupon_results/', EstoreCouponResultsView.as_view(), name='estore_coupon_results'),
    path('gallery_coupon_results/', GalleryCouponResultsView.as_view(), name='gallery_coupon_results'),
    path('hotdeals_coupon_results/', HotDealsCouponResultsView.as_view(), name='hotdeals_coupon_results')
]