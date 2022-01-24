from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Importacion de Serializadores
from Registro.serializers import UserSerializer


class RegistroView(APIView):
    def post(self, request):
        serializer =  UserSerializer(data = request.data) 
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
# Create your views here.
