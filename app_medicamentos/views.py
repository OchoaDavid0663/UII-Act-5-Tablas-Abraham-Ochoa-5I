from django.shortcuts import render

# Create your views here.
from .models import medicamentos

def index(request):
    medicamento = medicamentos.objects.all()
    return render(request, 'index.html', {'medicamentos': medicamento})

