from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
	context = {}
	return render(request, 'salas/index.html', context)

def loginAdmin(request):
	return HttpResponse("Login para usuario identificado como admin")

def loginEmpleado(request):
	return HttpResponse("Login para usuario identificado como empleado")