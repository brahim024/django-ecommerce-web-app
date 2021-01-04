from django.urls import path
from .import views
from .import api
app_name='ecomapp'
urlpatterns=[
    path('',views.product_list,name='product_list'),
    path('<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
 	#url from apis
 	path('api/product',api.product_list_api,name='product_list_api'),
 	path('api/<int:id>',api.product_detail,name='product_detail'),

]
