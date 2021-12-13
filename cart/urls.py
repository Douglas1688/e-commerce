from django.urls import path
from .views import *

urlpatterns = [
    path('',cart, name='cart'),
    path("add-cart/<int:product_id>/",add_cart, name="add-cart")
]