from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class CIN(models.Model):
    """
    Modèle central représentant une Carte d'Identité Nationale.
    Gère le cycle de vie de la donnée de la saisie à la validation.
    """
    class Statut(models.TextChoices):
        EN_ATTENTE = 'EN_ATTENTE', _('En attente de validation')
        VALIDE = 'VALIDE', _('Validé et Prêt pour impression')
        A_MODIFIER = 'A_MODIFIER', _('À modifier par l\'opérateur')

    # Identifiant unique et moteur de recherche
    numero_cin = models.CharField(
        max_length=12,
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r'^\d{12}$',
                message=_("Le numéro de CIN doit comporter exactement 12 chiffres."),
                code='invalid_cin_format'
            )
        ],
        verbose_name=_("Numéro de CIN")
    )

    # Preuves numériques (Images source)
    scan_recto = models.ImageField(
        upload_to='scans/recto/%Y/%m/',
        verbose_name=_("Scan Face Recto")
    )
    scan_verso = models.ImageField(
        upload_to='scans/verso/%Y/%m/',
        verbose_name=_("Scan Face Verso")
    )

    # Informations Identitaires - Section Recto
    photo_identite = models.ImageField(
        upload_to='photos/identite/%Y/%m/',
        verbose_name=_("Portrait d'identité")
    )
    
    is_duplicata = models.BooleanField(
        default=False,
        verbose_name=_("Type Duplicata")
    )
    date_remplacement = models.DateField(
        null=True,
        blank=True,
        verbose_name=_("Date de remplacement")
    )
    lieu_remplacement = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name=_("Lieu de remplacement")
    )
    
    nom = models.CharField(max_length=150, verbose_name=_("Nom patronymique"))
    prenom = models.CharField(max_length=150, verbose_name=_("Prénom(s)"))
    date_naissance = models.DateField(verbose_name=_("Date de naissance"))
    lieu_naissance = models.CharField(max_length=255, verbose_name=_("Lieu de naissance"))
    signe_particulier = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Signes particuliers visibles")
    )

    # Informations Sociales & Filiation - Section Verso
    domicile = models.CharField(max_length=255, verbose_name=_("Adresse de domicile"))
    arrondissement = models.CharField(max_length=100, verbose_name=_("Arrondissement"))
    profession = models.CharField(max_length=100, verbose_name=_("Profession / État"))
    nom_pere = models.CharField(max_length=255, verbose_name=_("Identité du Père"))
    nom_mere = models.CharField(max_length=255, verbose_name=_("Identité de la Mère"))
    
    date_creation = models.DateField(verbose_name=_("Date de délivrance originelle"))
    lieu_creation = models.CharField(max_length=255, verbose_name=_("Lieu de délivrance"))

    # Workflow de gestion
    statut = models.CharField(
        max_length=20,
        choices=Statut.choices,
        default=Statut.EN_ATTENTE,
        verbose_name=_("État du dossier")
    )
    motif_modification = models.TextField(
        null=True,
        blank=True,
        verbose_name=_("Notes de rejet / Instructions de modification")
    )

    # Métadonnées système
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Date de soumission"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Dernière mise à jour"))

    @property
    def numero_cin_parts(self):
        """Retourne le numéro CIN sous forme de 4 blocs de 3 chiffres"""
        val = str(self.numero_cin)
        if len(val) == 12:
            return [val[0:3], val[3:6], val[6:9], val[9:12]]
        return [val, "", "", ""]

    @property
    def date_naissance_fr(self):
        if not self.date_naissance:
            return ""
        months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        d = self.date_naissance
        return f"{d.day:02d} {months[d.month - 1]} {d.year}"

    @property
    def date_creation_fr(self):
        if not self.date_creation:
            return ""
        months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
        d = self.date_creation
        return f"{d.day:02d} {months[d.month - 1]} {d.year}"

    class Meta:
        verbose_name = _("CIN")
        verbose_name_plural = _("CINs")
        ordering = ['-created_at']

    def __str__(self):
        return f"CIN {self.numero_cin} | {self.nom.upper()} {self.prenom}"
