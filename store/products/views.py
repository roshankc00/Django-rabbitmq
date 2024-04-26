from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .producer import publish
import json

class ProductView(APIView):
    def post(self,request,pk=None,format=None):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            publish('product_created', json.dumps(serializer.data))
            return Response({'success':True,'message':'Product created successfully'},status=status.HTTP_201_CREATED)           
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)        
        
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu=Product.objects.get(id=pk)
            serializer=ProductSerializer(stu)
            return Response(serializer.data)
        else:
            product=Product.objects.all()
            serializer=ProductSerializer(product,many=True)
            return Response(serializer.data)               
    def delete(self, request,pk=None,format=None):
        if pk is not None:
          task=Product.objects.get(pk=pk)
          task.delete()
          return Response({'message':"Product Deleted successfully"})        
        else:
            return Response({'message':"Id field is required"},status=status.HTTP_400_BAD_REQUEST) 
    def patch(self,request,pk=None,format=None):
        if pk is not None:
            task=Product.objects.get(pk=pk)
            serializer=ProductSerializer(task,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':" Product Updated successfully"}) 
        else:
            return Response({'message':"Id field is required"},status=status.HTTP_400_BAD_REQUEST)     
        