from django.db import models

# Create your models here.
class SegundaTabla(models.Model):
    nombre= models.CharField(max_length=50, null=False)
    edad= models.IntegerField(default=0,null=False)
    direccion= models.CharField(max_length=50, null=False)
    numero=  models.IntegerField(default=0,null=False)
    imagen= models.ImageField(blank='',default="", upload_to='imagenes/')
    


    class Meta:
        managed = True
        db_table = 'usuarios_datos'