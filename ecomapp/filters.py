import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
	class Meta:
		model=Product
		fields='__all__'
		exclude=['category','slug','image','description','price','available','created','updated']