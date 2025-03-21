from django.db import models

# Create your models here.
class Persona(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido_paterno = models.CharField(max_length=50)
    Apellido_materno= models.CharField(max_length=50)
    Rut = models.CharField(max_length=10)
    Telefono = models.CharField(max_length=15)
    Correo = models.EmailField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)

class Cliente(Persona):
    
    def __str__(self):
        return f"{self.Nombre}"
    
class Mascota(models.Model):
    Nombre = models.CharField(max_length=50)
    Raza = models.CharField(max_length=50)
    Color = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Especie = models.CharField(max_length=50)
    Peso = models.FloatField(max_length=3)
    Edad = models.CharField(max_length=50)
    Id_cliente = models.ForeignKey(Cliente ,on_delete = models.CASCADE)
    # clave Foránea se hace sola
    # cascade = cuando se borra la id de la otra tabla se borra el campo de esta
    def __str__(self):
        return f"{self.Nombre} - {self.Especie} - {self.Raza} - {self.Sexo}"

class Veterinario(Persona):
    Especialidad = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.Nombre}"

class Consulta(models.Model):
    Fecha_hora = models.DateTimeField()
    Motivo = models.CharField(max_length=200)
    VeterinarioId = models.ForeignKey(Veterinario,on_delete = models.CASCADE)
    MascotaId = models.ForeignKey(Mascota, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.Fecha_hora}"


class Diagnostico(models.Model):
    Descripcion = models.CharField(max_length=200)
    Fecha_hora = models.DateTimeField()
    ConsultaId = models.ForeignKey(Consulta, on_delete= models.CASCADE)
    def __str__(self):
        return f"{self.Fecha_hora}"