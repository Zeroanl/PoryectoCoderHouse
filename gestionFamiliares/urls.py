from django.urls import path
from gestionFamiliares import views

urlpatterns = [
    
    path('home', views.home, name="Home"),
    path('Familiares', views.familiares, name="Familiares"),
]