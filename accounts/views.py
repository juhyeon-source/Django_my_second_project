from django.shortcuts import render
from rest_framework.views import APIView

from accounts.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class AccountSignupAPIView(APIView):
    
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
