from django.urls import  path
from . import views

app_name='payments'

urlpatterns=[
		path('process/',views.payment_process,name='payment_process'),
		path('done/',views.payment_done,name='payment_done'),
		path('canceled/',views.payment_canceled,name='payments_canceled'),
]