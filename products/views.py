import random

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.views import APIView
# Creatfe your views here.
from .produces import *
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Products.objects.all()
        serializers = ProductsSerializer(products, many=True)

        return Response(serializers.data)
    def create(self, request):
        serializer = ProductsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_created", serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def read(self, request, pk=None):
        product = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(product)
        return Response(serializer.data, status="status.")

    def update(self, request, pk=None):
        product = Products.objects.get(pk=pk)
        serializer = ProductsSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish("product_updated", serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Products.objects.get(pk=pk)
        product.delete()
        publish("product_deleted", pk)
        return Response(status=status.HTTP_200_OK)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })