from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.
def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    product=Pruduct.objetcs.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        product=Product.objetcs.filter(category=category)
    return render(request,'stor/product/list.html',
                            {'category':category,
                            'categories':categories,
                            'product':product})

def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    return render(request,'stor/product/details.html')
