from django.shortcuts import render, redirect,get_object_or_404
import braintree
from django.urls import reverse
from django.conf import settings
from order import Order 
# Create your views here.
gateway=braintree.BraintreeGateway(setting.BRAINTREE_CONF)
def payment_processing(request):
	order_id=request.session.get('order_id')
	order=get_object_or_404(Order,id=order_id)
	total_cost=order.get_total_cost()
	if request.method='POST':
		# nonce
		result=gateway.transaction.sale({
			'amount':f'{total_cost:.2f}',
			'payment_mathod_nonce':nonce,
			'options':{
				'submit_for_settlement':True
			}
		})
	if result.is_success:
		order.paid=True
		order.braintree_id=result.transaction.id
		order.save()
		return redirect('payment:done')
	else:
		client_token=gateway.client_token.generate()
		return render(request,'process.html',{'order':order,'client_token':client_token})
