import os
import sys
from xhtml2pdf import pisa

def generate_pdf():
    # Définition des chemins
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_pdf_path = os.path.join(base_dir, 'TERMES_DE_REFERENCE.pdf')
    media_pdf_path = os.path.join(base_dir, 'media', 'TERMES_DE_REFERENCE.pdf')

    # CSS et Structure HTML adaptés pour xhtml2pdf (support des règles @page, @frame, etc.)
    html_content = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
    @page {
        size: a4;
        margin-top: 2.5cm;
        margin-bottom: 2.5cm;
        margin-left: 2cm;
        margin-right: 2cm;
        @frame header {
            -pdf-frame-content: page-header;
            top: 1cm;
            left: 2cm;
            right: 2cm;
            height: 1cm;
        }
        @frame footer {
            -pdf-frame-content: page-footer;
            bottom: 1cm;
            left: 2cm;
            right: 2cm;
            height: 1cm;
        }
    }
    
    @page cover {
        size: a4;
        margin-top: 0cm;
        margin-bottom: 0cm;
        margin-left: 0cm;
        margin-right: 0cm;
        @frame header {
            -pdf-frame-content: none;
        }
        @frame footer {
            -pdf-frame-content: none;
        }
    }

    body {
        font-family: 'Helvetica', 'Arial', sans-serif;
        font-size: 10pt;
        line-height: 1.5;
        color: #333333;
    }

    /* Styles pour la Page de Couverture */
    .cover-container {
        padding: 3cm 2.5cm 2.5cm 2.5cm;
        background-color: #0c1a30;
        color: #ffffff;
    }
    
    .cover-header {
        text-align: center;
        margin-bottom: 2cm;
    }
    
    .republic-text {
        font-size: 9pt;
        letter-spacing: 2px;
        text-transform: uppercase;
        color: #C5A059;
        font-weight: bold;
        margin-bottom: 5px;
    }
    
    .motto-text {
        font-size: 8pt;
        font-style: italic;
        color: #a0aec0;
    }
    
    .cover-middle {
        margin-top: 3cm;
        margin-bottom: 4cm;
        text-align: center;
    }
    
    .cover-title {
        font-size: 26pt;
        font-weight: bold;
        line-height: 1.2;
        color: #ffffff;
        margin-bottom: 15px;
        text-transform: uppercase;
    }
    
    .cover-divider {
        border-top: 4px solid #C5A059;
        width: 150px;
        margin: 20px auto;
    }
    
    .cover-subtitle {
        font-size: 13pt;
        color: #a0aec0;
        letter-spacing: 1px;
    }
    
    .cover-footer {
        margin-top: 2cm;
        border-top: 1px solid #2d3748;
        padding-top: 1.5cm;
    }
    
    .metadata-table {
        font-size: 9pt;
    }
    
    .metadata-label {
        color: #a0aec0;
        font-weight: bold;
    }
    
    .metadata-value {
        color: #ffffff;
    }

    /* En-tête et pied de page */
    #page-header {
        font-size: 8pt;
        color: #718096;
        border-bottom: 1px solid #e2e8f0;
        padding-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    #page-footer {
        font-size: 8pt;
        color: #718096;
        border-top: 1px solid #e2e8f0;
        padding-top: 5px;
    }

    /* Style du contenu principal */
    h1 {
        font-size: 18pt;
        color: #043B70;
        font-weight: bold;
        margin-top: 0px;
        margin-bottom: 15px;
        border-bottom: 2px solid #C5A059;
        padding-bottom: 5px;
        text-transform: uppercase;
        page-break-after: avoid;
    }

    h2 {
        font-size: 13pt;
        color: #0c1a30;
        font-weight: bold;
        margin-top: 25px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }
    
    h3 {
        font-size: 11pt;
        color: #043B70;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 8px;
        page-break-after: avoid;
    }

    p {
        margin-top: 0px;
        margin-bottom: 12px;
        text-align: justify;
    }

    .page-break {
        page-break-before: always;
    }

    ul, ol {
        margin-top: 0px;
        margin-bottom: 15px;
        padding-left: 20px;
    }

    li {
        margin-bottom: 6px;
    }

    /* Tableaux de contenu */
    .content-table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 15px;
        margin-bottom: 15px;
    }

    .content-table th {
        background-color: #043B70;
        color: #ffffff;
        font-weight: bold;
        text-align: left;
        padding: 8px 10px;
        font-size: 9pt;
        border: 1px solid #043B70;
        text-transform: uppercase;
    }

    .content-table td {
        padding: 8px 10px;
        font-size: 9pt;
        border: 1px solid #cbd5e0;
    }

    .highlight-box {
        background-color: #f7fafc;
        border-left: 4px solid #C5A059;
        padding: 12px 15px;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    
    .highlight-box p:last-child {
        margin-bottom: 0px;
    }

    .badge {
        padding: 2px 6px;
        border-radius: 3px;
        font-size: 8pt;
        font-weight: bold;
        text-transform: uppercase;
    }
    
    .badge-primary {
        background-color: #ebf8ff;
        color: #2b6cb0;
    }

    .badge-success {
        background-color: #f0fff4;
        color: #2f855a;
    }

    .badge-warning {
        background-color: #fffaf0;
        color: #dd6b20;
    }
</style>
</head>
<body>

<!-- PAGE 1 : PAGE DE GARDE INSTITUTIONNELLE -->
<div class="page-break" style="page-break-before: avoid; page-template: cover;">
    <div class="cover-container">
        <div class="cover-header">
            <div class="republic-text">Repoblikan'i Madagasikara</div>
            <div class="motto-text">Fitiavana - Tanindrazana - Fandrosoana</div>
            <div style="border-top: 1px solid #C5A059; width: 80px; margin: 8px auto;"></div>
            <div class="republic-text" style="font-size: 8pt; margin-top: 5px; color: #a0aec0;">Ministère de l'Intérieur et de la Décentralisation</div>
        </div>
        
        <div class="cover-middle">
            <div class="cover-title">TERMES DE RÉFÉRENCE</div>
            <div class="cover-subtitle" style="font-size: 16pt; color: #C5A059; font-weight: bold;">PROJET DIGICIN</div>
            <div style="border-top: 4px solid #C5A059; width: 150px; margin: 15px auto;"></div>
            <div class="cover-subtitle" style="text-transform: uppercase; font-size: 10pt; letter-spacing: 2px;">
                Cadrage Stratégique, Spécifications Techniques et Financières<br>
                du Système National de Saisie et de Validation des Identités
            </div>
        </div>
        
        <div class="cover-footer">
            <table class="metadata-table">
                <tr>
                    <td class="metadata-label" width="180">DOCUMENT :</td>
                    <td class="metadata-value">Termes de Référence (TDR) d'infrastructure logicielle</td>
                </tr>
                <tr>
                    <td class="metadata-label" width="180">VERSION :</td>
                    <td class="metadata-value">v1.2 - Consolidation d'Architecture Pure Django</td>
                </tr>
                <tr>
                    <td class="metadata-label" width="180">STATUT :</td>
                    <td class="metadata-value">Approuvé pour l'étape de développement</td>
                </tr>
                <tr>
                    <td class="metadata-label" width="180">AUTEURS :</td>
                    <td class="metadata-value">Expert en Gestion de Projet &amp; Architecte Solution Senior</td>
                </tr>
                <tr>
                    <td class="metadata-label" width="180">DATE DE PRODUCTION :</td>
                    <td class="metadata-value">20 mai 2026</td>
                </tr>
                <tr>
                    <td class="metadata-label" width="180">DESTINATAIRE :</td>
                    <td class="metadata-value">Direction Générale de la Gestion des Identités et de l'État Civil</td>
                </tr>
            </table>
        </div>
    </div>
</div>

<!-- CONFIGURATION DES HEADER / FOOTER POUR LE RESTE DU DOCUMENT -->
<div id="page-header">MINISTÈRE DE L'INTÉRIEUR - PROJET DIGICIN - TERMES DE RÉFÉRENCE</div>
<div id="page-footer">
    Confidentiel - Usage Interne Gouvernemental &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Page <pdf:pagenumber/> sur <pdf:pagecount/>
</div>

<!-- PAGE 2 : CONTEXTE ET OBJECTIFS DU PROJET -->
<div class="page-break">
    <h1>1. Contexte et Objectifs du Projet</h1>
    
    <h2>1.1 Contexte National et Raison d'être</h2>
    <p>
        La gestion physique et décentralisée de l'état civil à Madagascar, s'appuyant historiquement sur des registres papier et des procédures hautement manuelles, fait face aujourd'hui à des limites insurmontables en termes de sécurité, d'efficacité administrative et de lutte contre la falsification. Les délais nécessaires au traitement des demandes de Cartes d'Identité Nationales (CIN) s'étendent fréquemment sur plusieurs semaines, pénalisant l'accès des citoyens à leurs droits constitutionnels fondamentaux, aux services financiers et à l'exercice démocratique.
    </p>
    <p>
        De surcroît, le manque de traçabilité des opérations de saisie et de validation accroît considérablement les risques d'erreurs d'écriture, d'usurpations d'identités et de doubles attributions de numéros. L'absence d'outils numériques souverains empêche un rapprochement réactif entre les fiches de demande et les pièces justificatives fournies.
    </p>
    
    <div class="highlight-box">
        <p><strong>Note d'importance stratégique :</strong></p>
        <p>
            Le projet <strong>DIGICIN</strong> a pour ambition de pallier ces défaillances systémiques en concevant une infrastructure logicielle étatique moderne, centralisée, robuste et souveraine. En s'appuyant sur l'architecture standard du framework Django et sur un fonctionnement MVT (Modèle-Vue-Template) strict et autosuffisant, la plateforme garantit des performances optimales sans aucune dépendance logicielle vis-à-vis d'éditeurs tiers étrangers ou de technologies complexes non maîtrisées.
        </p>
    </div>

    <h2>1.2 Objectif Général du Projet</h2>
    <p>
        L'objectif macro-institutionnel de DIGICIN est d'instituer une plateforme unifiée de numérisation, d'analyse, de validation décisionnelle et de production des Cartes d'Identité Nationales pour le territoire malagasy. La plateforme vise à doter les services administratifs centraux et déconcentrés d'un outil d'évaluation rigoureux, transparent et sécurisé pour dématérialiser intégralement le cycle de vie des identités.
    </p>

    <h2>1.3 Objectifs Spécifiques (S.M.A.R.T)</h2>
    <ul>
        <li>
            <strong>S (Spécifique) :</strong> Structurer et déployer quatre espaces exclusivement étanches au sein du même projet Django :
            <br>&bull; Un <em>portail public</em> d'information et de suivi pour le citoyen.
            <br>&bull; Un <em>pôle de saisie</em> dédié aux Opérateurs avec masques d'intégrité interactifs.
            <br>&bull; Un <em>centre décisionnel</em> de vérification split-screen pour les Contrôleurs.
            <br>&bull; Un <em>back-office</em> complet d'administration de la base de données gouvernementale.
        </li>
        <li>
            <strong>M (Mesurable) :</strong> 
            <br>&bull; Réduction du temps moyen de traitement d'un dossier de CIN à <strong>moins de 48 heures</strong> ouvrées.
            <br>&bull; Abaissement du taux d'erreur de saisie à <strong>moins de 0,5%</strong> grâce aux contrôles JS natifs et aux validateurs de schémas.
            <br>&bull; Assurer la traçabilité complète de <strong>100%</strong> des actions d'approbations et de rejet avec enregistrement des motifs.
        </li>
        <li>
            <strong>A (Atteignable) :</strong> Développement basé sur la pile standard python-django, SQLite pour les environnements de test et PostgreSQL pour le déploiement sur serveurs physiques sécurisés locaux, garantissant une souveraineté logicielle absolue et une maintenance simplifiée par les équipes locales.
        </li>
        <li>
            <strong>R (Réaliste) :</strong> Modélisation fidèle des pratiques administratives existantes (gestion différenciée du recto/verso, prise en compte des fiches de duplicata, des adresses de domicile, de la profession et de la filiation directe).
        </li>
        <li>
            <strong>T (Temporellement défini) :</strong> Phase de cadrage, de codage, de tests d'intrusion, de pilotage opérationnel d'agents municipaux et de mise en production effective délimitée sur une durée ferme de **90 jours calendaires**.
        </li>
    </ul>
</div>

<!-- PAGE 3 : DEFINITION DES BESOINS SPECIFIQUES -->
<div class="page-break">
    <h1>2. Définition des Besoins Spécifiques</h1>
    
    <h2>2.1 Besoins Fonctionnels par Profil Utilisateur</h2>
    
    <h3>A. Profil Citoyen (Utilisateur Public)</h3>
    <ul>
        <li><strong>Suivi de Demande Réactif :</strong> Possibilité de saisir son numéro de CIN à 12 chiffres sur une interface épurée pour en connaître l'état d'avancement.</li>
        <li><strong>Zéro Authentification Requise :</strong> Ce service public d'interrogation doit être directement utilisable par le citoyen sans qu'il ait besoin de créer un compte.</li>
        <li><strong>Transparence Institutionnelle :</strong> Affichage en clair du statut administratif (<em>Validé</em>, <em>En attente de traitement</em>, ou <em>À corriger</em> avec mention du motif de modification formulé par le contrôle).</li>
    </ul>

    <h3>B. Profil Opérateur (Agent de Saisie)</h3>
    <ul>
        <li><strong>Espace de Travail Isolé :</strong> Accès sécurisé à l'application de saisie après authentification sélective par mot de passe et choix explicite du pôle "Saisie".</li>
        <li><strong>Formulaire Structuré de Saisie :</strong> Enregistrement des données de la CIN structuré en sections visuelles : justificatifs (photo d'identité, scans recto et verso originaux), section "Recto" et section "Verso".</li>
        <li><strong>Contrôles Ergonomiques Réactifs (Vanilla JS) :</strong> 
            <br>&bull; Masquage/Affichage automatique des champs de duplicata optionnels (date et lieu de remplacement) selon l'état de la case "Duplicata".
            <br>&bull; Masque de saisie de la CIN avec formattage visuel automatique de l'index (`000 000 000 000`) pour éviter les erreurs de lecture.
            <br>&bull; Contrôle exclusif en temps réel du bouton de validation, s'activant uniquement lorsque l'ensemble des contrôles d'intégrité sont satisfaits.
        </li>
    </ul>

    <h3>C. Profil Contrôleur (Agent de Validation)</h3>
    <ul>
        <li><strong>Sélection et Authentification :</strong> Connexion via le pôle cible "Contrôle". Redirection vers le tableau de bord des dossiers en attente.</li>
        <li><strong>Analyse Tactique Comparée (Spit-screen) :</strong> Affichage scindé affichant à gauche les pièces justificatives numérisées de haute résolution, et à droite la maquette de la pièce d'identité finale générée textuellement.</li>
        <li><strong>Arbre de Décision Décisionnel :</strong> Possibilité de marquer le dossier comme `VALIDE` (gelant l'enregistrement d'identité) ou `A_MODIFIER` (imposant l'écriture obligatoire d'un motif complet de correction via une fenêtre modale).</li>
        <li><strong>Génération du Document d'État :</strong> Accès exclusif à la fonctionnalité d'export PDF officiel pour l'impression finale pour les CIN validées.</li>
    </ul>

    <h2>2.2 Besoins Non-Fonctionnels et Spécifications Techniques</h2>
    
    <table class="content-table">
        <thead>
            <tr>
                <th width="150">Domaine Technique</th>
                <th width="350">Spécifications et Normes de Sécurité</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td><strong>Architecture Applicative</strong></td>
                <td>Modèle Django MVT 100% pur. Rendu côté serveur strict (SSR) empêchant l'exposition des API et l'exposition d'endpoints vulnérables aux scripts.</td>
            </tr>
            <tr>
                <td><strong>Herméticité des Rôles</strong></td>
                <td>Ségrégation logique absolue. Utilisation des décorateurs <code>@user_passes_test</code> et des filtres personnalisés. Un opérateur ne peut accéder au dashboard de contrôle et vice versa.</td>
            </tr>
            <tr>
                <td><strong>Performance Base de Données</strong></td>
                <td>SGBD relationnel robuste PostgreSQL. Utilisation d'un index unique, index de recherche composite et validateurs de contraintes d'intégrité de clé.</td>
            </tr>
            <tr>
                <td><strong>Fichiers Médias</strong></td>
                <td>Traitement dynamique pour la gestion d'images (formatage, redimensionnement et sécurisation d'accès par la librairie Python Pillow).</td>
            </tr>
            <tr>
                <td><strong>Impression Documentaire</strong></td>
                <td>Mise en page vectorielle stricte et uniforme via xhtml2pdf et ReportLab.</td>
            </tr>
        </tbody>
    </table>
</div>

<!-- PAGE 4 : LES CONTRAINTES DU TRIANGLE D'OR -->
<div class="page-break">
    <h1>3. Les Contraintes du Triangle d'Or</h1>
    
    <h2>3.1 Axe Coût : Enveloppe budgétaire et ressources</h2>
    <p>
        Pour assurer la réussite de l'infrastructure nationale <strong>DIGICIN</strong>, le projet dispose d'une enveloppe de financement globale estimée à <strong>150 000 000 MGA (Ariary) Hors Taxes</strong>. Ce budget est structuré de la manière suivante :
    </p>

    <table class="content-table">
        <thead>
            <tr>
                <th width="260">Description du Poste Budgétaire</th>
                <th width="100">Pourcentage</th>
                <th width="140">Montant Évalué (MGA)</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Ingénierie logicielle Django, UI/UX et intégration de sécurité</td>
                <td align="center">53%</td>
                <td align="right">80 000 000 MGA</td>
            </tr>
            <tr>
                <td>Infrastructures de test et architecture de production</td>
                <td align="center">20%</td>
                <td align="right">30 000 000 MGA</td>
            </tr>
            <tr>
                <td>Audit technique et tests d'intrusion indépendants</td>
                <td align="center">13%</td>
                <td align="right">20 000 000 MGA</td>
            </tr>
            <tr>
                <td>Formation administrative, manuels et déploiement terrain</td>
                <td align="center">14%</td>
                <td align="right">20 000 000 MGA</td>
            </tr>
            <tr style="font-weight: bold; background-color: #f7fafc;">
                <td>TOTAL ESTIMÉ HORS TAXES</td>
                <td align="center">100%</td>
                <td align="right">150 000 000 MGA</td>
            </tr>
        </tbody>
    </table>

    <h2>3.2 Axe Délai : Calendrier et Chronologie des Jalons</h2>
    <p>
        Le développement et le déploiement opérationnel de DIGICIN sont encadrés par un calendrier strict de <strong>90 jours ouvrés</strong> répartis selon les 5 jalons cardinaux suivants :
    </p>
    
    <ol>
        <li><strong>Jalon 1 (J0 à J20) :</strong> Modélisation et structure de base de données. Écriture du modèle de données de la CIN unique, mise en œuvre des validateurs logiques de champs (validateurs d'unicité, expressions régulières pour le format à 12 chiffres) dans l'application core.</li>
        <li><strong>Jalon 2 (J21 à J45) :</strong> Finalisation du Pôle de Saisie. Développement et intégration des formulaires d'enregistrement avec interactions de validation asynchrones natives (Vanilla JS), gestion du duplicata dynamique et validation visuelle réactive du numéro CIN.</li>
        <li><strong>Jalon 3 (J46 à J65) :</strong> Module de Validation Décisionnelle &amp; Module d'Impression Documentaire. Conception de l'interface en split-screen pour les contrôleurs et écriture du moteur d'impression PDF sécurisé basé sur xhtml2pdf.</li>
        <li><strong>Jalon 4 (J66 à J80) :</strong> Consolidation de la sécurité et intégration globale. Mise en œuvre des filtres de rôles (Opérateurs, Contrôleurs) lors du processus de connexion, tests unitaires et mise en place de la recherche citoyenne.</li>
        <li><strong>Jalon 5 (J81 à J90) :</strong> Recette technique, formation des utilisateurs et Go-Live. Configuration initiale des environnements par script automatisé (comptes pilotes), correction finale des bugs d'intégration et lancement officiel.</li>
    </ol>

    <h2>3.3 Axe Qualité : Normes de Développement et d'Acceptance</h2>
    <ul>
        <li><strong>Normes de codage de haut niveau :</strong> Respect absolu de la directive PEP 8 pour l'écriture de l'ensemble du code Python de l'infrastructure. Typage fort des contrôles et refus des lignes abrégées ou tronquées.</li>
        <li><strong>Durabilité technologique :</strong> Architecture "No Tech-Larping" (Refus des décorations visuelles non sollicitées, des terminaux ou de logs superflus). Restreindre l'ensemble des interactions au service d'une clarté à vocation professionnelle.</li>
        <li><strong>Critères d'homologation :</strong> Zero vulnérabilité d'isolation de rôles constatée lors des audits de sécurité. Validation systématique du format d'impression de la carte d'identité sur le PDF généré par les contrôleurs administratifs.</li>
    </ul>
</div>

</body>
</html>
"""

    try:
        # Étape 1 : Enregistrement du PDF principal à la racine
        with open(output_pdf_path, "wb") as pdf_file:
            pisa_status = pisa.CreatePDF(html_content, dest=pdf_file)
            
        if pisa_status.err:
            print("❌ Erreur de génération du PDF principal.")
            return False
            
        print(f"✓ PDF principal généré à : {output_pdf_path}")
        
        # Étape 2 : Enregistrement d'une copie dans le dossier media de Django (si existant)
        os.makedirs(os.path.dirname(media_pdf_path), exist_ok=True)
        with open(media_pdf_path, "wb") as pdf_file_media:
            pisa.CreatePDF(html_content, dest=pdf_file_media)
            
        print(f"✓ Copie du PDF enregistrée dans le dossier des médias à : {media_pdf_path}")
        return True

    except Exception as e:
        print(f"❌ Erreur inattendue : {str(e)}")
        return False

if __name__ == "__main__":
    generate_pdf()
