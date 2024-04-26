from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.

class TestView(APIView):
    # oneway to communication
    def get(self,request,format=None):
        print()
        