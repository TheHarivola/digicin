from django.urls import path
from . import views

app_name = 'citoyen'

urlpatterns = [
    path('recherche/', views.cin_search_view, name='search'),
]
