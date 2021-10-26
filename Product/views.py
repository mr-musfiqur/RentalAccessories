from django.shortcuts import render
from .models import Product


def product(request):
    products = Product.objects.all()
    list_products =[]
    for x in products:
        text = '/media/' + str(x.picture)
        print(text)
        dict = {
            'name': x.name,
            'price': x.price,
            'img': text,


        }
        list_products.append(dict)
    return render(request, 'product/product.html', {'products': list_products})
