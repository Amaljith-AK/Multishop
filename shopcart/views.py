from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cartlist(request, tot=0, count=0, ct_items=None):
    try:
        ct = CartList.objects.get(card_id=cart_no(request))
        ct_items = Items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.offerprice * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 'tot': tot, 'count': count})


def cart_no(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = Products.objects.get(id=product_id)
    try:
        ct = CartList.objects.get(card_id=cart_no(request))
    except CartList.DoesNotExist:
        ct = CartList.objects.create(card_id=cart_no(request))
        ct.save()
    try:
        c_items = Items.objects.get(prodt=prod, cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity += 1
        c_items.save()
    except Items.DoesNotExist:
        c_items = Items.objects.create(prodt=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cartdetails')


def del_cart(request, product_id):
    ct = CartList.objects.get(card_id=cart_no(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = Items.objects.get(prodt=prod , cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def removeall_cart(request, product_id):
    ct = CartList.objects.get(card_id=cart_no(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartdetails')
