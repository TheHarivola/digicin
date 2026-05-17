🚀 Étape 1 : Récupérer le projet
Ouvre ton terminal (ou CMD) et clone le dépôt :
code
Bash
git clone https://github.com/ton-utilisateur/digicin.git
cd digicin


🛠 Étape 2 : Créer l'environnement virtuel
Il est crucial d'isoler les dépendances du projet pour éviter les conflits.
Sur Windows :
code
Bash
python -m venv venv
venv\Scripts\activate
Sur macOS / Linux :
code
Bash
python3 -m venv venv
source venv/bin/activate


📦 Étape 3 : Installer les dépendances
Une fois l'environnement activé (tu devrais voir (venv) au début de ta ligne de commande), installe les bibliothèques nécessaires :
code
Bash
pip install --upgrade pip
pip install -r requirements.txt


🗄 Étape 4 : Préparer la base de données
Maintenant, crée la structure de la base de données locale (SQLite par défaut) :
code
Bash
python manage.py makemigrations core operateur controlleur citoyen
python manage.py migrate


🔑 Étape 5 : Configuration initiale (Groupes et Utilisateurs)
Lance le script spécial que nous avons créé pour configurer automatiquement les rôles (Opérateurs/Contrôleurs) et créer les comptes de test :
code
Bash
python initial_setup.py
Identifiants créés par défaut :
Admin : admin / admin123
Opérateur : op1 / mdp123
Contrôleur : ctrl1 / mdp123


📸 Étape 6 : Dossier des médias
Django a besoin d'un dossier pour stocker les photos et les scans de CIN :
Le dossier media/ se créera automatiquement lors du premier upload, mais assure-toi d'avoir les droits d'écriture dans le dossier du projet.


📽 Étape 7 : Lancer le serveur
Enfin, démarre l'application :
code
Bash
python manage.py runserver
Ouvre ton navigateur sur : http://127.0.0.1:8000


💡 Aide-mémoire des commandes Python importantes
Action	Commande
Lancer le serveur	python manage.py runserver
Appliquer des changements de modèles	python manage.py makemigrations puis migrate
Créer un autre super-admin	python manage.py createsuperuser
Entrer dans le shell Django	python manage.py shell
Quitter l'environnement virtuel	deactivate
⚠️ Note sur les images (macOS/Linux)
Si tu rencontres une erreur liée à Pillow (images) sur Mac ou Linux, tu devras peut-être installer les bibliothèques système de gestion d'image avant le pip install :
Mac : brew install jpeg zlib
Ubuntu/Debian : sudo apt-get install libjpeg-dev zlib1g-dev