from celery import task
from django.core.mail import send_mail
from.models import Order

@task
def order_craeted(order_id):
	order=Order.objects.get(id=order_id)
	subject=f'Order nr. {order.id}'
	message=f'Dear {order.first_name},\n\n'\
			f'You have succesfely placed an order.'\
			f'Your orde ID is {oredr.id}.'
	send_mail=send_mail(subject,message,'admin000@gmail.com',[order.email])
	return mail_sent
	