from dataclasses import fields
from rest_framework import routers, serializers, viewsets
#Importancion de modelos
from LoadImage.models  import TablaArchivos

class TablaArchivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaArchivos
        fields= ('id','name_img','url_img', 'format_img')