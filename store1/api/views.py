from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .producer2 import PublishAndGet
# Create your views here.

class TestView(APIView):
    # oneway to communication
    def get(self,request,format=None):
        product=PublishAndGet(1)    
        print(product)    
        return Response(product)
        