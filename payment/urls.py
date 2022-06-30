from django.urls import path, include
from . import views

app_name = 'payments'
urlpatterns = [
    path('starter/', views.starter, name='starter'),
    path('compact/', views.compact, name='compact'),
    path('compact_plus/', views.compact_plus, name='compact_plus'),
    path('premium/', views.premium, name='premium')
]