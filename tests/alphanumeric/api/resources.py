from tastypie.fields import CharField
from tastypie.resources import ModelResource
from alphanumeric.models import Product


class ProductResource(ModelResource):
    
    class Meta:
        resource_name = 'products'
        queryset = Product.objects.all()
