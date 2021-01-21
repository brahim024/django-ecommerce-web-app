from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import CommentForm
from .filters import ProductFilter
# Create your views here.
def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    product=Product.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        product=product.filter(category=category)
    myfilter=ProductFilter(request.GET,queryset=Product.objects.all())
    return render(request,'list.html',
                          {'category':category,
                            'categories':categories,
                            'products':product,'myfilter':myfilter})
def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    comments=product.comment.filter(active=True)
    new_comment=None
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.product=product
            new_comment.save()
            #return HttpResponseRedirect('stor/product_list_by_category')
        
    else:
        form=CommentForm()
    context={'form':form,'product':product,
             'cart_product_form':cart_product_form,
             'new_comment':new_comment,
             'comments':comments,}
    return render(request,'details.html',context)
