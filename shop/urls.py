

from django.urls import path
from .import views

urlpatterns = [
    path('', views.index,name='ShopeHome'),
    path('about/', views.about,name='About'),
    path('contact/', views.contact,name='contactUs'),
    path('tracker/', views.tracker,name='TrackingStatus'),
    path('search/', views.search,name='Search'),
    path('productview/', views.prodView,name='ProductView'),
    path('checkout/', views.checkout,name='CheckOut'),
]