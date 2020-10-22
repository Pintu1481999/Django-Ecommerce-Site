from django.shortcuts import render
from django.http import HttpResponse
# from shop.models import Product
from .models import Product ## Here we used only ".models" bcz it's already in 'shop'.
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = (n // 4) + ceil((n / 4) - (n // 4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = (n // 4) + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    
    # params = {'no_of_slides': nSlides, 'range': range(1, nSlides), 'product': products}
    # allProds = [[products, range(1, len(products)), nSlides],
    #             [products, range(1, len(products)), nSlides]]
    params = {'allProds': allProds} 
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')
    # return HttpResponse('Test')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, id):
    return render(request, 'shop/prodView.html')

def checkout(request):
    return render(request, 'shop/checkout.html')

def contact(request):
    return render(request, 'shop/contact.html')
