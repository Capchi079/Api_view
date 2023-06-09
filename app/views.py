from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


@permission_classes([IsAuthenticated])
class Product_data(APIView):
    def get(self,request):
        PO=Product.objects.all()
        PJO=ProductJData(PO,many=True)
        return Response(PJO.data)

    def post(self,request):
        PMSD= ProductJData(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'product is created'})
        else:
            return Response({'failedd':'oroduct is not created'})
    def put(self,request):
        pid=request.data['Pid']
        productobjects=Product.objects.get(Pid=pid)
        PMSD=ProductJData(productobjects,data=request.data)
        if PMSD.is_valid():
            PMSD.save()
            return Response({'mes':'sucessfull update data'})
        return Response({'failed':'not updatedd'})