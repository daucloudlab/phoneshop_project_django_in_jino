from django.shortcuts import render
from models import Products
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def test(request):
    return HttpResponse('OK!!!!')

@csrf_exempt
def create(request):
    fname = request.POST['name']
    str_price = request.POST['price']
    fprice = float(str_price)
    fdescription = request.POST['description']
    if (fname is None) or (str_price is None) or (fdescription is None):
        result = json.dumps({'success': 0, 'message' : 'ERROR!!!!.'})
    else:
        products = Products(name = fname, price = fprice, description = fdescription)
        products.save()
        result = json.dumps({'success': 1, 'message' : 'Product successfully created.'})

    return HttpResponse(result)


def get_product_detail(request):
    pid = request.GET['pid']
    product = Products.objects.get(pk = pid)
    if product is None:
        result = json.dumps({'success': 0, 'message' : 'No Product Found.'})
    else:
        pid = product.id
        name = product.name
        price = product.price
        description = product.description
        result = json.dumps({'success': 1, 'message' : 'query OK.',
                             'product':[{'pid':pid, 'name':name, 'price':price,
                                         'description':description}]})

    return HttpResponse(result)

def get_all_products(request):
    products = Products.objects.all()
    if products is None:
        result = json.dumps({'success': 0, 'message' : 'No Product Found.'})
    else:
        product_list = []
        for product in products:
            pid = product.id
            name = product.name
            price = product.price
            description = product.description
            product_list.append({'pid':pid, 'name':name, 'price':price,'description':description})

        result = json.dumps({'success': 1, 'message' : 'query OK.',
                             'product':product_list})

    return HttpResponse(result)

@csrf_exempt
def update_product(request):
    pid = request.POST['pid']
    product = Products.objects.get(pk = pid)

    if product is None:
        result = json.dumps({'success': 0, 'message' : 'Required field(s) is missing.'})
    else:
        fname = request.POST['name']
        str_price = request.POST['price']
        fprice = float(str_price)
        fdescription = request.POST['description']

        product.name = fname
        product.price = fprice
        product.description = fdescription

        product.save()
        result = json.dumps({'success': 1, 'message' : 'Product successfully updated.'})

    return HttpResponse(result)

@csrf_exempt
def delete_product(request):
    pid = request.POST['pid']
    product = Products.objects.get(pk = pid)
    if product is None:
        result = json.dumps({'success': 0, 'message' : 'No Product Found.'})
    else:
        product.delete()
        result = json.dumps({'success': 1, 'message' : 'Product successfully deleted.'})

    return HttpResponse(result)

def create_test(request):
    return render(request, 'phoneshop/create_test.html')