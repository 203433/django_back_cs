from django.urls import path, re_path
from django.conf.urls import include


from componenteImagen.views import SegundaTablaJson

urlpatterns = [
    re_path(r'imagen/', SegundaTablaJson.as_view()),    
]
