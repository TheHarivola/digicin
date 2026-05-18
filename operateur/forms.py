from django import forms
from core.models import CIN

class CINForm(forms.ModelForm):
    """
    Formulaire de saisie pour l'opérateur.
    Inclut des styles Tailwind personnalisés et des validations logiques avancées.
    """
    numero_cin = forms.CharField(
        max_length=15, 
        label="Numéro de CIN",
        widget=forms.TextInput(attrs={
            'placeholder': '000 000 000 000',
            'maxlength': '15',
            'id': 'id_numero_cin'
        })
    )

    class Meta:
        model = CIN
        exclude = ['statut', 'motif_modification']
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'date_creation': forms.DateInput(attrs={'type': 'date'}),
            'date_remplacement': forms.DateInput(attrs={'type': 'date'}),
            'signe_particulier': forms.Textarea(attrs={'rows': 2}),
            'is_duplicata': forms.CheckboxInput(attrs={'class': 'w-5 h-5 text-blue-600 border-2 border-slate-300 rounded focus:ring-blue-500 transition-all cursor-pointer'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Application globale des styles Tailwind pour une UI cohérente
        for field_name, field in self.fields.items():
            if field_name == 'is_duplicata':
                continue
            
            # Classes de base pour tous les inputs
            base_classes = "w-full p-4 bg-slate-50 border border-slate-200 rounded-xl text-slate-800 placeholder-slate-400 focus:bg-white focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm font-medium outline-none"
            
            if isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({
                    'class': 'block w-full text-xs text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-xs file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 transition-all cursor-pointer'
                })
            else:
                field.widget.attrs.update({'class': base_classes})

    def clean_numero_cin(self):
        """
        Nettoie et valide le format du numéro CIN.
        Supprime les espaces et vérifie la longueur.
        """
        data = self.cleaned_data.get('numero_cin')
        if data:
            data = data.replace(' ', '')
            if not data.isdigit() or len(data) != 12:
                raise forms.ValidationError("Le numéro de CIN doit comporter exactement 12 chiffres.")
        return data

    def clean(self):
        """
        Validation croisée pour les dossiers de type duplicata.
        """
        cleaned_data = super().clean()
        is_duplicata = cleaned_data.get('is_duplicata')
        date_remplacement = cleaned_data.get('date_remplacement')
        lieu_remplacement = cleaned_data.get('lieu_remplacement')

        if is_duplicata:
            if not date_remplacement or not lieu_remplacement:
                msg = "Pour un duplicata, la date et le lieu de remplacement sont obligatoires."
                if not date_remplacement:
                    self.add_error('date_remplacement', msg)
                if not lieu_remplacement:
                    self.add_error('lieu_remplacement', msg)
        
        return cleaned_data
