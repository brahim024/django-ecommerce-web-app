from django.shortcuts import render, redirect ,get_object_or_404
from django.views.decorator.http import require_POST
from ecomapp.models import Product
from.cart import Cart  #this is Cart class in cart.py
from .forms import CartAddProductForm
# Create your views here.
@require_POST
def cart_adding(request,product_id):
    cqrt=Cart(request)
    product=get_object_or_404(Prodyct,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        cd=form.clean_data
        cart.add(product=product,
                quantity=cd['quantity'],
                override_quantity=cd['override'])
    return redirect('cart':cart_details)
