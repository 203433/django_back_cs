from django.urls import path, re_path
from django.conf.urls import include


from LoadImage.views import TablaArchivosMultiParser


urlpatterns = [
    re_path(r'archivo/', TablaArchivosMultiParser.as_view()),    
]
