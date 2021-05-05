from django.shortcuts import render
from .models import Servicio
# Create your views here.
def services(request):
    servicios = Servicio.objects.all()
    return render(request, 'services/services.html', {'servicios':servicios})
