from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def product_list_api(request):
	all_product=Product.objects.all()
	data=ProductSerializer(all_product,many=True).data
	return Response({'data':data})
def product_detail(request,id):
	product_detail=Product.get(id=id)
	data=ProductSerializer(product_detail).data
	return Response({'data':data})