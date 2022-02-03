from multiprocessing import context
from urllib import response
from primerComponente import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions

#Importancion de modelos
from LoadImage.models import TablaArchivos
from LoadImage.serializers import TablaArchivosSerializer

# Create your views here.
class TablaArchivosMultiParser (APIView):
    #parser_classes = (FormParser, MultiPartParser,)

    def post(self, request):
        if 'imagen' not in request.data:
            raise exceptions.ParseError(
                "No has seleccionado el archivo a subir")

        archivos = str(request.FILES)

        #archivos = str(request.FILES.getlist('imagen'))

        # return Response({'data':str(request.data),'file':archivos},status=status.HTTP_201_CREATED)
        serializer = TablaArchivosSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            datos = TablaArchivos(**validated_data)
            datos.save()

            serializer_response = TablaArchivosSerializer(datos)

            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)