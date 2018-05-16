from django.db import models

# Create your models here.

class Usuario(models.Model):
	usuario_id = models.IntegerField(primary_key=True)
	usuario_name = models.CharField(max_length=75)
	usuario_pass = models.CharField(max_length=12)
	usuario_role = models.IntegerField()
	usuario_mail = models.CharField(max_length=200)

class Sala(models.Model):
	sala_id = models.IntegerField(primary_key=True)
	sala_name = models.CharField(max_length=50)
	sala_location = models.CharField(max_length=50)
	sala_status = models.IntegerField()
	sala_capacity = models.IntegerField()

class Horario(models.Model):
	horario_id = models.IntegerField(primary_key=True)
	horario_idsala = models.IntegerField()
	horario_date = models.DateField()
	horario_time = models.TimeField()
	horario_status = models.IntegerField()

class Insumo(models.Model):
	insumo_id = models.IntegerField(primary_key=True)
	insumo_idsala = models.IntegerField()
	insumos_name = models.CharField(max_length=50)

class Reserva(models.Model):
	reserva_id = models.IntegerField(primary_key=True)
	reserva_date = models.DateField()
	reserva_starttime = models.TimeField()
	reserva_endtime = models.TimeField()
	reserva_capacity = models.IntegerField()
	reserva_idinsumo = models.IntegerField()
	reserva_idsala = models.IntegerField() 