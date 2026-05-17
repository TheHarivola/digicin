# DIGICIN - Système de Gestion d'Identité National

DIGICIN est une application Django modulaire permettant la saisie (Opérateur) et la validation (Contrôleur) des Cartes d'Identité Nationales avec génération de PDF sécurisé.

---

### 🚀 Étape 1 : Récupérer le projet
Ouvrez votre terminal (ou CMD) et clonez le dépôt :
```bash
git clone https://github.com/ton-utilisateur/digicin.git
cd digicin
```

---

### 🛠 Étape 2 : Créer l'environnement virtuel
Il est crucial d'isoler les dépendances pour éviter les conflits.

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```

**Sur macOS / Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 Étape 3 : Installer les dépendances
Une fois l'environnement activé (vous devriez voir `(venv)` au début de votre ligne de commande) :
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

### 🗄 Étape 4 : Préparer la base de données
Initialisez la structure de la base de données locale (SQLite par défaut) :
```bash
python manage.py makemigrations core operateur controlleur citoyen
python manage.py migrate
```

---

### 🔑 Étape 5 : Configuration initiale (Rôles & Utilisateurs)
Lancez le script de configuration pour créer automatiquement les groupes et les comptes de test :
```bash
python initial_setup.py
```

**Identifiants créés par défaut :**
| Rôle | Identifiant | Mot de passe |
| :--- | :--- | :--- |
| **Administrateur** | `admin` | `admin123` |
| **Opérateur** | `op1` | `mdp123` |
| **Contrôleur** | `ctrl1` | `mdp123` |

---

### 📸 Étape 6 : Gestion des fichiers médias
Le dossier `media/` (exclu du Git) contiendra les photos et scans de CIN. Assurez-vous d'avoir les droits d'écriture dans le dossier.

---

### 📽 Étape 7 : Lancer le serveur
Démarrer l'application :
```bash
python manage.py runserver
```
Accédez à l'application via : [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 💡 Aide-mémoire des commandes utiles

| Action | Commande |
| :--- | :--- |
| **Lancer le serveur** | `python manage.py runserver` |
| **Changements de modèles** | `python manage.py makemigrations` puis `migrate` |
| **Créer un autre super-admin** | `python manage.py createsuperuser` |
| **Entrer dans le shell Django** | `python manage.py shell` |
| **Quitter l'environnement** | `deactivate` |

---

### ⚠️ Note sur la gestion d'images (macOS/Linux)
Si vous rencontrez une erreur liée à **Pillow**, installez les bibliothèques système :
*   **Mac :** `brew install jpeg zlib`
*   **Ubuntu/Debian :** `sudo apt-get install libjpeg-dev zlib1g-dev`

