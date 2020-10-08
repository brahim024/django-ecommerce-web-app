from django.urls import reverse
from .tasks import order_created 
from django.shortcuts import render
from .models import OrderItem ,Order
from.forms import OrderCreateForm
from cart.cart import Cart
# Create your views here.
def order_add(request):
	cart=Cart(request)
	if request.method=='POST':
		form=OrderCreateForm(request.POST)
		if form.is_valid():
			order=form.save()
			for item in cart:
				OrderItem.objects.create(order=order,
										product=item['product'],
										price=item['price'],
										quantity=item['quantity']
										)

			cart.clear()
			# launch asynchro=nouse task
			order_created.delay(order.id)  #
			request.session['order_id']=order.id #
			return redirect(reverse('payment:process'))#
	else:
		form=OrderCreateForm()
	return render(request,'create.html',{'cart':cart,'form':form})