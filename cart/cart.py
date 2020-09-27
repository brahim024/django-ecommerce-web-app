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
