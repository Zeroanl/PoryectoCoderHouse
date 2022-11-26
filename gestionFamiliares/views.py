from django.shortcuts import render
from .models import Familiares


# Create your views here.

def home(request):
    return render(request,"gestionFamiliares/home.html")




def familiares(request):
    data = Familiares.objects.all()
    context = {'data': data}
    return render(request,"gestionFamiliares/Familiares.html",context)


