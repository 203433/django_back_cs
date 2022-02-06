from django.urls import path, re_path
from django.conf.urls import include


from LoadImage.views import TablaArchivosMultiParser
from LoadImage.views import TablaArchivosTabla

urlpatterns = [
    re_path(r'archivoPost/', TablaArchivosTabla.as_view()), 
    re_path(r'archivo/(?P<pk>\d+)$', TablaArchivosMultiParser.as_view()),    
]
