from django.shortcuts import render
from core.models import CIN

def cin_search_view(request):
    query = request.GET.get('q', '')
    cin = None
    error = None
    
    if query:
        # Nettoyage des espaces pour la recherche
        clean_query = query.replace(' ', '')
        try:
            cin = CIN.objects.get(numero_cin=clean_query)
        except CIN.DoesNotExist:
            error = "Aucun dossier trouvé pour ce numéro de CIN."
            
    return render(request, 'citoyen/search.html', {
        'cin': cin,
        'error': error,
        'query': query,
        'title': 'Suivi de Dossier CIN'
    })
