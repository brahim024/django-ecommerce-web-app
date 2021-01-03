from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .forms import CommentForm
# Create your views here.
def product_list(request,category_slug=None):
    category=None
    categories=Category.objects.all()
    product=Product.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        product=product.filter(category=category)
    return render(request,'list.html',
                            {'category':category,
                            'categories':categories,
                            'products':product})

def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    cart_product_form=CartAddProductForm()
    commnts=product.comment.filter(active=True)
    new_comment=None
    if request.mesthod=="POST":
        comment_form=CommentForm(data=requests.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.product=product
            new_comment.save()
        else:
            comment_form=CommentForm()
    return render(request,'details.html',{'product':product,'cart_product_form':cart_product_form,
                            'commnts':commnts,'comment_form':comment_form})