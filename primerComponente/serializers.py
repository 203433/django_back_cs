from dataclasses import fields
from rest_framework import routers, serializers, viewsets
#Importancion de modelos
from primerComponente.models import PrimerTabla
class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ('nombre','edad') 
        fields = ('__all__') 