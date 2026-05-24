from django.urls import path
from . import views

app_name = 'citoyen'

urlpatterns = [
    path('recherche/', views.cin_search_view, name='search'),
    path('tdr/pdf/', views.download_tdr_pdf_view, name='tdr_pdf'),
    path('cin/pdf/<int:pk>/', views.download_cin_pdf_view, name='download_pdf'),
]
