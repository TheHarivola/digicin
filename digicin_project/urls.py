from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

from django.shortcuts import redirect

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def form_valid(self, form):
        # On récupère le choix du rôle du formulaire
        target_role = self.request.POST.get('target_role')
        self.request.session['target_role'] = target_role
        return super().form_valid(form)

def smart_home_redirect(request):
    if request.user.is_authenticated:
        target = request.session.get('target_role')
        
        # Redirection basée sur le choix ET les droits réels
        if target == 'saisie' and (request.user.groups.filter(name='Opérateurs').exists() or request.user.is_superuser):
            return redirect('operateur:dashboard')
        elif target == 'controle' and (request.user.groups.filter(name='Contrôleurs').exists() or request.user.is_superuser):
            return redirect('controlleur:dashboard')
        
        # Fallback automatique si le choix n'est pas cohérent ou absent
        if request.user.groups.filter(name='Opérateurs').exists():
            return redirect('operateur:dashboard')
        elif request.user.groups.filter(name='Contrôleurs').exists():
            return redirect('controlleur:dashboard')
        elif request.user.is_superuser:
            return redirect('/admin/')
            
    return redirect('citoyen:search')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', CustomLoginView.as_view(), name='login'), # Vue personnalisée
    path('accounts/', include('django.contrib.auth.urls')), 
    path('operateur/', include('operateur.urls')),
    path('controlleur/', include('controlleur.urls')),
    path('citoyen/', include('citoyen.urls')),
    path('', smart_home_redirect, name='home'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
