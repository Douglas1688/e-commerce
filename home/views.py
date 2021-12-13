from django.shortcuts import render
from django.views.generic import DetailView
from store.models import Product
# Create your views here.

def home(request):
    prod = Product.objects.all().filter(is_available = True)
    context = {'products':prod}
    return render(request,'home/home.html',context)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'home/product-detail.html'