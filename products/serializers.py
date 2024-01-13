from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['title', 'price', 'content',
                  'my_price']

    def get_my_price(self, obj):
        return obj.sel_price
