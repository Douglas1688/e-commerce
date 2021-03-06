from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product
# Create your views here.

def store(request,category_slug = None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category = categories, is_available = True)
    else:
        products = Product.objects.all().filter(is_available = True)

    contexto = {
        'products':products
    }
    return render(request,'store/store.html',contexto)
