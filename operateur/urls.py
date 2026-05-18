from django.urls import path
from . import views

app_name = 'operateur'

urlpatterns = [
    path('', views.operateur_dashboard, name='dashboard'),
    path('nouveau/', views.cin_create_view, name='nouveau'),
    path('modifier/<int:pk>/', views.cin_update_view, name='modifier'),
]
