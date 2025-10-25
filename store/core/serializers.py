from rest_framework import serializers
from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields='__all__'

# Serializer : custome
# ModelSerializer : Automated from model
class ProductListSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=models.Product
        # fields=['name','price']
        fields='__all__'
        # exclude=''

class CartAddSerializer(serializers.Serializer):
    product_id=serializers.IntegerField()

    ## get json to up field, send user
    # def to_internal_value(self, data):
    #     ...

    ## send data server
    # def to_representation(self, card_item):
    #     ...

    # customize, change data to own field
    def __init__(self,data={},*args,**kwargs):
        d=[]
        for id, count in data.items():
            d.append({'id':id,'count':count})
        kwargs['many']=True
        super(CartAddSerializer,self).__init__(data=d,*args,**kwargs)
        self.is_valid()

class CartShowSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    count=serializers.IntegerField()
