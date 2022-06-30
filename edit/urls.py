from django.urls import path, include
from . import views

app_name = 'edit'
urlpatterns = [
    path('profile/', views.profile, name='profile')
]