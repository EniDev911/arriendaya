from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.TextField()
    correo = models.TextField()

class TipoInmueble(models.Model):
    tipo_inmueble = models.TextField()

class Comuna(models.Model):
    comuna = models.CharField(max_length=100)

class Region(models.Model):
    region = models.CharField(max_length=100)

class TipoUsuario(models.Model):
    tipo_user = models.TextField()

class Inmueble(models.Model):
    nombre_inmueble = models.TextField()
    descripcion = models.TextField()
    m2_construido = models.FloatField(default=0)
    m2_terreno = models.FloatField(default=0)
    direccion = models.CharField(max_length=200)
    numero_banos = models.IntegerField(default=0)
    numero_hab = models.IntegerField(default=0)
    numero_est = models.IntegerField(default=0)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    id_tipo_inmueble = models.ForeignKey(TipoInmueble, on_delete=models.CASCADE, null=True)
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, null=True)
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)