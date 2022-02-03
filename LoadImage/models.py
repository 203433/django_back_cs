from django.db import models
from django.utils import timezone

# Create your models here.
class TablaArchivos(models.Model):
    name_img = models.CharField(max_length=50, null=False)
    url_img = models.CharField(max_length=100, null=False)
    format_img= models.CharField(max_length=50, null=False)
    created= models.DateTimeField(default=timezone.now)
    edited= models.DateTimeField(blank=True,default=None,null=True)
    
    class Meta:
        managed = True
        db_table = 'tabla_archivos'