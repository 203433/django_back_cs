from multiprocessing import context
from urllib import response
from django.shortcuts import render
from primerComponente import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


# importaciones de modelos agregados
from primerComponente.models import PrimerTabla

# importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here

responseOk =  '{ "messages":"success", "pay_load": "serializer.data", "status" : "status"}'

responseOk = json.loads(responseOk)

'{ "messages":"success", "pay_load": "serializer.data", "status" : "status"}'




class PrimerTablaList(APIView):
    def jsonMaker(self, message, data, status):
        json1 = {"message":message, "pay_load":data, "status":status }
        dumper=json.dumps(json1)
        response_ok = json.loads(dumper)
        return response_ok


    def get(self, request, format=None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializer(queryset, many = True, context = {'request':request})
        response_ok = self.jsonMaker("succes", serializer.data, status.HTTP_200_OK)
        return Response(response_ok)

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class PrimerTablaDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerTabla.objects.get(pk = pk)
        except PrimerTabla.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        id_response = self.get_object(pk)
        if id_response != 0:
            id_response = PrimerTablaSerializer(id_response)
            return Response(id_response.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)

    def put(self, request,pk, format=None):
        id_response = self.get_object(pk)
        serializer = PrimerTablaSerializer(id_response, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 


    def delete(self, request, pk, format=None):
        objetive = self.get_object(pk)
        if objetive!="No existe":
            objetive.delete()
            return Response("Dato eliminado" ,status=status.HTTP_200_OK)
        else:
            return Response("Dato no encontrado",status=status.HTTP_400_BAD_REQUEST)


