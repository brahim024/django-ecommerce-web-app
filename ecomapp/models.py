from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ecomapp:product_list_by_category',args=[self.slug])
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    name=models.CharField(max_length=40,db_index=True)
    slug=models.SlugField(max_length=100,db_index=True)
    image=models.ImageField(upload_to='products/%Y',blank=True)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        index_together=(('id','slug'),)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('ecomapp:product_detail',args=[self.id,self.slug])
class Comment(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comment')
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    class Meta:
        ordering=('created',)
    def __str__(self):
        return f'Comment By {self.name}on {self.product}'
