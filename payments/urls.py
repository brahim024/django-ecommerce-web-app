from django.urls import  path
from . import views

app_name='payments'

urlpatterns=[
		path('process/',views.process,name='process'),
		path('done/',views.done,name='done'),
		path('canceled/',views.canceled,name='canceled'),
]