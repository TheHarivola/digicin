from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from core.models import CIN
from .forms import CINForm

def is_operateur(user):
    return user.is_authenticated and (user.groups.filter(name='Opérateurs').exists() or user.is_superuser)

@user_passes_test(is_operateur)
def cin_create_view(request):
    """
    Gère la saisie d'une nouvelle demande de CIN par l'opérateur.
    Rendu serveur pur avec notifications de statut.
    """
    if request.method == 'POST':
        form = CINForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Dossier enregistré avec succès. Transmission au centre de contrôle effectuée.")
            return redirect('operateur:dashboard')
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = CINForm()
    
    context = {
        'form': form,
        'title': 'Nouvelle Demande CIN'
    }
    return render(request, 'operateur/form.html', context)

@user_passes_test(is_operateur)
def operateur_dashboard(request):
    """Tableau de bord de l'opérateur pour voir les dossiers à corriger."""
    # Tri personnalisé : A_MODIFIER en premier, puis EN_ATTENTE, puis VALIDE
    from django.db.models import Case, When, Value, IntegerField
    
    cins = CIN.objects.all().annotate(
        priority=Case(
            When(statut='A_MODIFIER', then=Value(1)),
            When(statut='EN_ATTENTE', then=Value(2)),
            When(statut='VALIDE', then=Value(3)),
            default=Value(4),
            output_field=IntegerField(),
        )
    ).order_by('priority', '-updated_at')
    
    context = {
        'cins': cins,
        'title': 'Mon Tableau de Bord'
    }
    return render(request, 'operateur/dashboard.html', context)

@user_passes_test(is_operateur)
def cin_update_view(request, pk):
    """Permet à l'opérateur de corriger un dossier rejeté."""
    cin = get_object_or_404(CIN, pk=pk)
    
    if cin.statut != 'A_MODIFIER':
        messages.error(request, "Ce dossier ne peut plus être modifié.")
        return redirect('operateur:dashboard')

    if request.method == 'POST':
        form = CINForm(request.POST, request.FILES, instance=cin)
        if form.is_valid():
            cin_obj = form.save(commit=False)
            cin_obj.statut = 'EN_ATTENTE' 
            cin_obj.save()
            messages.success(request, "Corrections enregistrées. Le dossier est renvoyé en contrôle.")
            return redirect('operateur:dashboard')
    else:
        form = CINForm(instance=cin)
    
    return render(request, 'operateur/form.html', {
        'form': form, 
        'cin': cin,
        'title': f'Correction CIN #{cin.numero_cin}'
    })
