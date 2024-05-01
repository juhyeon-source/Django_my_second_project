from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductListAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        request.data['author'] = request.user.id
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProductDetailAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(request, id):
        return get_object_or_404(Product, id=id)

    def get(self, request, id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
        
    def put(self, request, id):
        product = self.get_object(id)
        if request.user != product.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        request.data['author'] = request.user.id
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
    def delete(self, request, id):
        product = self.get_object(id)
        if request.user != product.author:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        product.delete()
        data = {"delete": f"Product({id}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)