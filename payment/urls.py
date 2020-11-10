from django.urls import path
app_name='payment'
from.import views
urlpatterns=[
	path('process/',views.payment_processing,name='process'),
	path('done/',views.payment_done,name='done'),
	path('cancel/',views.payment_canceled,name='cancel'),


]