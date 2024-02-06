from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductDetails, Tag
from .serializers import ProductSerializer, ProductDetailsSerializer, TagSerializer

class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()[:5]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        product_details = ProductDetails.objects.get(product_id=product_id)
        serializer = ProductDetailsSerializer(product_details)
        return Response(serializer.data, status=status.HTTP_200_OK)

