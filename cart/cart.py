from decimal import Decimal
from django.conf import settings
from ecomapp.models import Product

class Cart(object):
    def __init__(self.request):
        self.sessions=request.sessions
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[setting.CART_SESSION_ID]={}
        self.cart=cart
    def add(self,product,quantity=1,override_quantity=False):
        #add product to the cart and update items quantity
        product_id=str(product.id)
        if product_id not in (product.id):
            self.cart[product_id]={'quantity':0,
                                    'price':str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity']=quantity
        else:
            self.cart[product_id]['quantity']+=quantity
    def save(self):
        self.session.modified=True
    def remove(self,product):
        product_id= str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(id__in=product_ids)
        cart=self.cart.copy()
        for product in products:
            cart[str(product.id)]['product']=product
        for item in cart.value():
            item['price']=Decimal(item['price'])
            item['total_prie']=item['price'] * item['quantity']
            yield item
    def __len__(self):
        return sum(Decimal(tem['price'])) * item['quantity'] for item in self.cart.value())
    def clear(self):
        deg self.session[setting.CART_SESSION_ID]
        self.save()
