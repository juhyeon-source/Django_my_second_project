from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework import status



@api_view(["GET","POST"])
def product_list(request):
    if request.method=="GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    elif request.method == "PUT":
        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == "DELETE":
        product.delete()
        data = {"delete": f"Product({id}) is deleted."}
        return Response(data, status=status.HTTP_200_OK)