from django.shortcuts import render

# Create your views here.

from multiprocessing import context
from urllib import response
from primerComponente import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


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
            # Convertir y guardar el modelo
            editorial = SegundaTabla(**validated_data)
            editorial.save()

            serializer_response = SegundaTablaSerializer(editorial)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        