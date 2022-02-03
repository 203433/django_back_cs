from django.urls import path, re_path
from django.conf.urls import include


from componenteImagen.views import SegundaTablaJson
from componenteImagen.views import SegundaTablaMuliParser

urlpatterns = [
    re_path(r'imagen/', SegundaTablaJson.as_view()),    
    re_path(r'imagenHTML/', SegundaTablaMuliParser.as_view()),    
]
