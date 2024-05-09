from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.

def get_info(request):
    categories = Category.objects.all()
    contex = {
        'categories': categories
    }
    return render(request, 'index.html', context=contex)

def get_products(request, pk):
    products = Product.objects.filter(category=pk)
    contex = {
        'products': products
    }
    return render(request, 'products.html', context=contex)

def detail(request, pk):
    product = Product.objects.filter(category=pk)
    context = {
        'product': product
    }
    return render(request, 'detail.html', context=context)







