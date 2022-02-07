from multiprocessing import context
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView
from rest_framework import status
import os.path
#Importancion de modelos
from LoadImage.models import TablaArchivos
from LoadImage.serializers import TablaArchivosSerializer

# Create your views here.
class TablaArchivosTabla(APIView):
    def get(self, request, format=None):
        queryset = TablaArchivos.objects.all()
        serializer = TablaArchivosSerializer(queryset, many = True, context = {'request':request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No hay archivo para subir")
        archivos = request.data['url_img']
        name, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = name
        request.data['format_img'] = formato
        serializer = TablaArchivosSerializer(data=request.data)
        # return Response({'data': str(request.data)})
        if serializer.is_valid():
            validated_data = serializer.validated_data
            # Convertir y guardar el modelo
            img = TablaArchivos(**validated_data)
            img.url_img =  '127.0.0.1:8000/assets/img/' + str(img.url_img)
            img.save()
            serializer_response = TablaArchivosSerializer(img)
            return Response(serializer_response.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TablaArchivosMultiParser(APIView):
    def get_object(self, pk):
        try:
            return TablaArchivos.objects.get(pk = pk)
        except TablaArchivos.DoesNotExist:
            return 0

    def get(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = TablaArchivosSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        serializer = TablaArchivosSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        imagen = self.get_object(pk)
        if imagen != 0:
            imagen.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response("Dato no encontrado",status = status.HTTP_400_BAD_REQUEST)