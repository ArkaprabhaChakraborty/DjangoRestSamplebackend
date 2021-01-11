from django.shortcuts import render
from rest_framework import viewsets
from .models import Product ,User
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
import random as rd
# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many = True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk = None):
        product = Product.objects.get(id = pk)
        serializers = ProductSerializer(product)
        return Response(serializers.data)

    def update(self, request, pk = None):
        product  = Product.objects.get(id = pk)
        serializer = ProductSerializer(instance = product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk = None):
        product = Product.objects.get(id = pk)
        product.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.object.all()
        user = rd.choice(users)
        return Response({
            'id': user.id
        }) 