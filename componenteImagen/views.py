from django.shortcuts import render

# Create your views here.

from multiprocessing import context
from urllib import response
from primerComponente import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions


# importaciones de modelos agregados
from componenteImagen.models import SegundaTabla
from componenteImagen.serializers import SegundaTablaSerializer

class SegundaTablaJson(APIView):
    def get(self, request, *args):
        print(str(self.parser_classes))
        return Response({'parsers': ' '.join(map(str, self.parser_classes))}, status=204)

    def post(self, request):
        serializer = SegundaTablaSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            archivo = validated_data['imagen']
            archivo.name = 'imagen.png'
            validated_data['imagen'] = archivo
            # Convertir y guardar el modelo
            datos = SegundaTabla(**validated_data)
            datos.save()

            serializer_response = SegundaTablaSerializer(datos)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

# Enviado por medio de HTML Form
class SegundaTablaMuliParser(APIView):
    #parser_classes = (FormParser, MultiPartParser,)

    def post(self, request):
        if 'imagen' not in request.data:
            raise exceptions.ParseError(
                "No has seleccionado el archivo a subir")

        archivos = str(request.FILES)

        #archivos = str(request.FILES.getlist('imagen'))

        # return Response({'data':str(request.data),'file':archivos},status=status.HTTP_201_CREATED)
        serializer = SegundaTablaSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            datos = SegundaTabla(**validated_data)
            datos.save()

            serializer_response = SegundaTablaSerializer(datos)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)