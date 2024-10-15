from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductDetails, Tag
from .serializers import ProductSerializer, ProductDetailsSerializer, TagSerializer

# Define a view to handle requests for the list of products
class ProductListView(APIView):
    # Handle GET requests to retrieve a list of products
    def get(self, request):
        # Fetch the first 5 products from the database
        products = Product.objects.all()[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailsView(APIView):
    # Handle GET requests to retrieve details of a product by its ID
    def get(self, request, product_id):
        product_details = ProductDetails.objects.get(product_id=product_id)
        serializer = ProductDetailsSerializer(product_details)
        return Response(serializer.data, status=status.HTTP_200_OK)
