from rest_framework import serializers
from .models import Product, ProductDetails, Tag, Review, RelatedProduct

# Serializer for Tag model to convert model instances to JSON format and validate input data
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'  

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' 

class ProductDetailsSerializer(serializers.ModelSerializer):
    product = ProductSerializer()  # Nesting ProductSerializer to include product details

    class Meta:
        model = ProductDetails
        fields = '__all__' 
