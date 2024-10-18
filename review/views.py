from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .mels import ProductReview
from .serializers import ProductReviewSerializerod

class ProductReviewView(APIView):
    def get(self, request, product_id):
        reviews = ProductReview.objects.filter(product_id=product_id)
        serializer = ProductReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

