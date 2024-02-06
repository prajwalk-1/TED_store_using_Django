from rest_framework import serializers
from .models import Product, ProductDetails, Tag, Review, RelatedProduct

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductDetails
        fields = '__all__'
