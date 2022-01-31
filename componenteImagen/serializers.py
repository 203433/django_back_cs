from dataclasses import fields
import base64
from drf_extra_fields.fields import Base64ImageField
from rest_framework import routers, serializers, viewsets
#Importancion de modelos
from componenteImagen.models import SegundaTabla
class SegundaTablaSerializer(serializers.ModelSerializer):

    imagen = Base64ImageField(required=False)

    class Meta:
        model = SegundaTabla
        fields= ('id','nombre','edad', 'direccion', 'imagen')