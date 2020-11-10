from django.shortcuts import render, redirect,get_object_or_404
import braintree
from django.urls import reverse
from django.conf import settings
from order.models import Order 
# Create your views here.
gateway=braintree.BraintreeGateway(settings.BRAINTREE_CONF)
def payment_processing(request):
	order_id=request.session.get('order_id')
	order=get_object_or_404(Order,id=order_id)
	total_cost=order.get_total_cost()
	if request.method=='POST':
		# nonce
		nonce=request.POST.get('payment_method_nonce',None)
		result=gateway.transaction.sale({
			'amount':f'{total_cost:.2f}',
			'payment_method_nonce':nonce,
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
			return redirect('payment:cancel')
	else:
		client_token=gateway.client_token.generate()
		return render(request,'process.html',{'order':order,'client_token':client_token})
def payment_done(request):
	return render(request,'done.html')

	
def payment_canceled(request):
	return render(request,'cancel.html')
