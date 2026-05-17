from django.contrib import admin
from .models import CIN

@admin.register(CIN)
class CINAdmin(admin.ModelAdmin):
    list_display = ('numero_cin', 'nom', 'prenom', 'statut', 'created_at')
    list_filter = ('statut', 'created_at')
    search_fields = ('numero_cin', 'nom', 'prenom')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Identifiant', {
            'fields': ('numero_cin', 'statut', 'motif_modification')
        }),
        ('Documents Scannés', {
            'fields': ('photo_identite', 'scan_recto', 'scan_verso')
        }),
        ('Identité Recto', {
            'fields': ('is_duplicata', 'date_remplacement', 'lieu_remplacement', 'nom', 'prenom', 'date_naissance', 'lieu_naissance', 'signe_particulier')
        }),
        ('Données Verso', {
            'fields': ('domicile', 'arrondissement', 'profession', 'nom_pere', 'nom_mere', 'date_creation', 'lieu_creation')
        }),
        ('Dates Système', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
