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
