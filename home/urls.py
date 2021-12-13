from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home, name='home'),
    path('product/<int:pk>/',ProductDetailView.as_view(),name='product-detail')
]