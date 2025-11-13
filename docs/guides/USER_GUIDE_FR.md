# Master Search - Guide d'Utilisation

**Version:** 2025.11.7  
**Dernière mise à jour:** 12 novembre 2025  
**Langues:** Français · Deutsch · English

---

## 📑 Table des matières

1. [Aperçu](#aperçu)
2. [Installation](#installation)
3. [Notions de base](#notions-de-base)
4. [Fonctionnalités principales](#fonctionnalités-principales)
5. [Techniques de recherche](#techniques-de-recherche)
6. [Rapports HTML](#rapports-html)
7. [Paramètres](#paramètres)
8. [Conseils et astuces](#conseils-et-astuces)
9. [FAQ](#faq)
10. [Dépannage](#dépannage)

---

## Aperçu

**Master Search** est un outil de bureau puissant pour la recherche complète de texte dans les systèmes de fichiers. Il permet une recherche rapide et efficace dans les fichiers et dossiers avec des options de filtrage avancées et de beaux rapports HTML.

### Que peut faire Master Search?

✅ **Recherche rapide de fichiers** - Recherche des millions de fichiers en secondes  
✅ **Recherche de contenu** - Recherche le contenu des fichiers  
✅ **Support des expressions régulières** - Expressions régulières pour les modèles complexes  
✅ **Rapports HTML** - Génération automatique de beaux rapports avec animations  
✅ **59+ types de fichiers** - Support du code, documents, archives et plus  
✅ **Multilingue** - Allemand, Anglais, Français  
✅ **Affichage en temps réel** - Voir les résultats à mesure qu'ils apparaissent  
✅ **Intégration du presse-papiers** - Copie en un clic des chemins de fichiers  

---

## Installation

### Windows MSI Installer (Recommandé)

1. **Télécharger** le dernier fichier MSI depuis la page de publication
2. **Double-cliquer** sur `Master_Search_Setup_v2025.11.7.msi`
3. **Suivre l'Assistant d'installation:**
   - Choisir le dossier d'installation (par défaut: `C:\Program Files\Master Search`)
   - Créer un raccourci du menu Démarrage (optionnel)
   - Créer un raccourci sur le bureau (optionnel)
4. **Terminer** - Master Search est prêt à être utilisé immédiatement

### Version portable

1. **Télécharger** le fichier ZIP portable
2. **Extraire** dans le répertoire souhaité
3. **Exécuter** `master_search.exe` (aucune installation requise)
4. **Optionnel:** Créer un raccourci sur le bureau

### Configuration système requise

| Exigence | Version |
|----------|---------|
| **Windows** | 7 SP1 ou plus récent |
| **Mémoire** | 512 Mo de RAM minimum |
| **Espace disque** | 100 Mo d'espace libre |
| **Navigateur** | Navigateur moderne pour les rapports HTML |

---

## Notions de base

### Interface utilisateur

L'interface GUI de Master Search comprend quatre zones principales:

```
┌─────────────────────────────────────────────────────────┐
│  Master Search v2025.11.7                         [_][□][X]│
├─────────────────────────────────────────────────────────┤
│  ZONE DE RECHERCHE                                      │
│  ┌────────────────────────────────────────────────────┐ │
│  │ Terme de recherche: [________________]              │ │
│  │ Filtre de type:     [Tous] [Code] [Documents]      │ │
│  │ Emplacement:        [C:\]  [Parcourir...]          │ │
│  │ ☐ Chercher dans fichiers  ☐ Casse sensible         │ │
│  │ ☐ Expressions régulières   ☐ Générer rapport       │ │
│  │                     [DÉMARRER RECHERCHE]            │ │
│  └────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│  RÉSULTATS EN TEMPS RÉEL                                │
│  ┌────────────────────────────────────────────────────┐ │
│  │ 💾 C:\Projects\README.md         [📋] [📂] [🗑️]   │ │
│  │ 💾 C:\Projects\config.json       [📋] [📂] [🗑️]   │ │
│  │ 📄 C:\Docs\rapport.docx          [📋] [📂] [🗑️]   │ │
│  │ Recherche en cours... 145 résultats trouvés         │ │
│  └────────────────────────────────────────────────────┘ │
├─────────────────────────────────────────────────────────┤
│ ✓ Terminé! 247 fichiers recherchés, 12 correspondances │
└─────────────────────────────────────────────────────────┘
```

### Éléments de l'interface

| Élément | Description |
|---------|-------------|
| **Terme de recherche** | Le mot ou la phrase que vous recherchez |
| **Filtre de type de fichier** | Limiter à des types de fichiers spécifiques (optionnel) |
| **Emplacement de recherche** | Répertoire à rechercher |
| **Chercher dans les fichiers** | Rechercher le contenu des fichiers (pas seulement les noms) |
| **Casse sensible** | Distinguer les majuscules des minuscules |
| **Expressions régulières** | Utiliser un motif regex au lieu d'un texte simple |
| **Générer rapport HTML** | Générer automatiquement un rapport après la recherche |

---

## Fonctionnalités principales

### 1. Recherche simple de fichiers

**Scénario:** Vous voulez trouver tous les fichiers Python nommés `test`

**Étapes:**
1. **Terme de recherche:** Entrez `test`
2. **Filtre de type:** Choisissez "Code"
3. **Emplacement:** Choisissez le répertoire racine ou `C:\`
4. **Cliquez [DÉMARRER RECHERCHE]**

**Résultat:**
- Tous les `.py`, `.js`, `.ts` etc. avec "test" dans le nom sont affichés
- Les résultats apparaissent en temps réel
- Après achèvement: Statistiques (par ex., "247 fichiers recherchés, 12 correspondances")

### 2. Recherche de contenu dans les fichiers

**Scénario:** Vous voulez trouver une fonction spécifique dans tous les fichiers de code

**Étapes:**
1. **Terme de recherche:** par ex., `def calculate_total`
2. **Filtre de type:** Choisissez "Code"
3. ☑️ **"Chercher dans les fichiers"** activer (important!)
4. **Emplacement:** Choisissez le répertoire du projet
5. **Cliquez [DÉMARRER RECHERCHE]**

**Résultat:**
- Seuls les fichiers contenant le texte sont affichés
- Le terme de recherche est mis en évidence dans le rapport
- Les numéros de ligne indiquent la position exacte du texte

### 3. Recherche avec expressions régulières (Utilisateurs avancés)

**Scénario:** Vous voulez trouver toutes les adresses e-mail dans les fichiers

**Étapes:**
1. **Terme de recherche:** `[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}`
2. ☑️ **"Expressions régulières"** activer
3. ☑️ **"Chercher dans les fichiers"** activer
4. **Filtre de type:** "Tous" (pour rechercher tous les types de fichiers)
5. **Cliquez [DÉMARRER RECHERCHE]**

**Motifs Regex populaires:**
```regex
# Adresses e-mail
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# Numéros de téléphone (France)
(\+33|0)[1-9]\d{8}

# Tailles de fichier (bytes, KB, MB, GB)
\d+\s*(B|KB|MB|GB|TB)

# Adresses IP
\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}

# URLs
https?://[^\s]+

# Tailles de fichier en JSON
"size"\s*:\s*(\d+)
```

### 4. Casse sensible

**Comportement par défaut:** La recherche ignore la casse
- `test` trouve: Test, TEST, tEsT

**Lorsqu'activé:** Considère les majuscules/minuscules
- `Test` trouve uniquement: Test (pas test ou TEST)

**Quand utiliser:**
- Variables de code: `myVariable` vs `myVariable`
- Noms de fichiers: `README` vs `readme`
- Configurations: Souvent sensibles à la casse!

---

## Techniques de recherche

### Plusieurs termes de recherche

Master Search supporte plusieurs termes de recherche séparés par des espaces:

```
Terme de recherche: function main utils
```

Cela trouve les fichiers contenant **tous** ces termes:
- ✅ `function main(utils)`
- ✅ `Utils class with main function`
- ❌ `function main` (manque "utils")

### Filtres de type de fichier

Catégories prédéfinies:

| Filtre | Types de fichiers |
|--------|------------------|
| **Code** | `.py`, `.js`, `.ts`, `.java`, `.cpp`, `.c#`, `.go`, `.rs` etc. |
| **Web** | `.html`, `.css`, `.php`, `.js`, `.vue`, `.jsx` etc. |
| **Données** | `.json`, `.xml`, `.yaml`, `.csv`, `.sql`, `.db` etc. |
| **Documents** | `.pdf`, `.docx`, `.xlsx`, `.pptx`, `.md`, `.txt` etc. |
| **Configuration** | `.ini`, `.cfg`, `.conf`, `.env`, `.properties` etc. |
| **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` etc. |

### Sélection de l'emplacement de recherche

**Sélection rapide:**
- `C:\` - Disque dur entier
- `C:\Users\` - Fichiers utilisateur uniquement
- `C:\Program Files\` - Programmes uniquement

**Chemin personnalisé:**
1. Cliquez sur **[Parcourir...]**
2. Sélectionnez le répertoire souhaité
3. Cliquez sur **OK**

**Conseils:**
- ⚡ Les répertoires plus étroits sont plus rapides
- 🔒 Les dossiers système (Windows, System32) sont souvent protégés en lecture seule
- 🚫 Les chemins réseau peuvent être lents

---

## Rapports HTML

### Que sont les rapports HTML?

Rapports générés automatiquement avec:
- 📊 **Statistiques** - Nombre de correspondances, fichiers recherchés
- 📁 **Catégories** - Aperçu par type de fichier
- ✨ **Animations** - Effets de fondu professionnels
- 🔗 **Liens interactifs** - Ouvrir les fichiers directement
- 📋 **Fonction presse-papiers** - Copier les chemins
- 🎨 **Design réactif** - Fonctionne sur tous les appareils

### Créer un rapport

**Automatiquement pendant la recherche:**
1. ☑️ **"Générer rapport HTML"** activer
2. Exécutez la recherche normalement
3. Après achèvement: Le rapport s'ouvre automatiquement

**Emplacement de stockage:**
```
C:\Users\<YourUsername>\AppData\Local\Master Search\Reports\
  ├── search_results_20251112_153249.html
  ├── search_results_20251112_153418.html
  └── search_results_20251112_154523.html
```

### Fonctionnalités des rapports

#### 📋 Copier dans le presse-papiers
- Cliquez sur un chemin de fichier dans le rapport
- Le chemin est automatiquement copié dans le presse-papiers
- Une notification confirme la copie réussie

#### 📂 Ouvrir le dossier
- Cliquez sur l'icône du dossier à côté d'un fichier
- Ouvre le dossier avec le fichier dans l'Explorateur

#### 🔍 Mise en évidence
Les termes de recherche sont mis en évidence:
- **Orange** - Termes de recherche trouvés
- **Ligne X** - Position exacte dans le texte

#### 📊 Aperçu des catégories
Analyse automatique:
```
📁 Types de fichiers
┌─────────────────────┐
│ Python        145   │
│ JSON           89   │
│ Markdown       54   │
│ YAML           28   │
│ XML            12   │
└─────────────────────┘
```

#### ✨ Animations
- Le rapport se charge avec un arrière-plan blanc
- Les éléments s'estompent séquentiellement
- Apparence professionnelle et polie
- Aucun impact sur les performances

---

## Paramètres

### Sélection de la langue

Master Search détecte automatiquement la langue système:
- 🇫🇷 **Français** - Windows en français
- 🇩🇪 **Deutsch** - Windows en allemand
- 🇬🇧 **English** - Windows en anglais

**Sélection manuelle:**
Dans la plupart des dialogues, cliquez sur "Langue" pour changer.

### Paramètres de performance

**Paramètres par défaut (optimal):**
- Multi-traitement actif
- Utilisation maximale du CPU
- Recherche la plus rapide

**Pour les PC plus lents:**
- Réduire les demandes matérielles
- Moins de threads de travail
- Recherche plus longue, mais plus stable

### Gestion des erreurs

Master Search ignore automatiquement:
- 🔒 **Fichiers protégés en lecture seule** - Pas de permission
- ⚠️ **Fichiers corrompus** - Ne peuvent pas être lus
- 🔁 **Liens symboliques/jonctions** - Empêcher les boucles infinies
- 🌐 **Erreurs réseau** - Lecteurs hors ligne

---

## Conseils et astuces

### ⚡ Recherches plus rapides

1. **Choisir des répertoires plus étroits**
   - Au lieu de `C:\` → utiliser `C:\Projects\`
   - 10x plus rapide!

2. **Utiliser les filtres de type de fichier**
   - Au lieu de "Tous" → uniquement "Code" ou "Documents"
   - Réduit les fichiers à rechercher de 70%

3. **Utiliser des termes plus spécifiques**
   - `function main` au lieu de `main`
   - Moins de correspondances = traitement plus rapide

### 🎯 Recherches plus précises

1. **Activer la casse sensible**
   - Quand vous avez besoin de correspondances exactes

2. **Utiliser des expressions régulières pour les modèles complexes**
   - `^import.*os$` - Uniquement les lignes `import os`
   - `def\s+\w+\(` - Toutes les définitions de fonctions

3. **Activer "Chercher dans les fichiers"**
   - Pour rechercher le contenu des fichiers au lieu de juste les noms

### 📊 Analyse des rapports

1. **Trier par type de fichier**
   - Les catégories du rapport montrent la distribution
   - Utile pour l'analyse de la structure du projet

2. **Recherche multilingue**
   - Allemand: `Ñame`, `Größe`
   - Anglais: `Name`, `Size`
   - Un rapport pour tous!

3. **Analyse des tendances**
   - Enregistrer plusieurs rapports
   - Comparer le nombre de fichiers au fil du temps

### 🛠️ Pour les développeurs

**Rechercher dans les projets Python:**
```
Terme de recherche: TODO
Filtre: Code
Chercher dans fichiers: ☑️
```

**Trouver tous les imports:**
```
Terme de recherche: ^import
Regex: ☑️
Filtre: Code
```

**Trouver les fichiers de configuration:**
```
Terme de recherche: api_key
Filtre: Configuration
Chercher dans fichiers: ☑️
```

---

## FAQ

### Q: Combien de temps prend une recherche?

**R:** Cela dépend de:
- **Taille du répertoire:** 1000 fichiers ≈ 1 seconde
- **Emplacement de recherche:** Disque local vs. réseau
- **Filtre de type de fichier:** Plus rapide avec filtre
- **Chercher dans les fichiers:** Plus lent que la recherche de nom uniquement

**Exemples:**
- `C:\Projects\` (10 000 fichiers): ~10 secondes
- `C:\` (500 000 fichiers): ~5 minutes
- Avec filtre: 2-3x plus rapide

### Q: Où sont stockés les rapports?

**R:**
```
Windows 7/8/10/11:
C:\Users\<YourUsername>\AppData\Local\Master Search\Reports\
```

**Ouvrir le dossier:**
1. Ouvrir l'interface → Clic droit sur le rapport
2. Cliquez sur "Ouvrir le dossier"
3. Voir tous les rapports

### Q: Puis-je annuler une recherche?

**R:** Oui!
- Pendant que la recherche est en cours: Le bouton **[ANNULER]** apparaît
- Cliquez dessus pour arrêter immédiatement
- Les résultats précédents sont conservés

### Q: Quelle est la différence entre "Chercher dans les fichiers" et le filtre normal?

**R:**
```
SANS "Chercher dans les fichiers":
  Recherche uniquement les noms de fichiers
  test.py ✅
  testing.txt ✅
  mytestfile.py ✅
  
AVEC "Chercher dans les fichiers":
  Recherche aussi le contenu des fichiers
  fichier_avec_test_dans_le_contenu.py ✅
  + tout ce qui précède aussi
```

### Q: Master Search supporte-t-il les caractères génériques?

**R:**
- **Recherche normale:** Non (mais vous pouvez utiliser des expressions régulières)
- **Avec expressions régulières:** Oui!
  - `test.*\.py` - test123.py, testfile.py, etc.
  - `\.log$` - Fichiers .log uniquement à la fin

### Q: Puis-je rechercher sur les lecteurs réseau?

**R:** Oui, mais:
- ✅ Les partages réseau SMB/CIFS fonctionnent
- ⚠️ Peut être lent (latence réseau)
- 🔒 Nécessite une permission d'accès
- 💡 **Conseil:** "Monter" le lecteur réseau localement pour de meilleures performances

### Q: Comment puis-je imprimer un rapport?

**R:**
1. Ouvrir le rapport dans le navigateur
2. Appuyez sur **Ctrl+P** (ou Fichier → Imprimer)
3. Choisir l'imprimante
4. ✓ Peut aussi enregistrer en PDF!

### Q: Quels types de fichiers sont supportés?

**R:** 59+ types de fichiers:
- **Code:** Python, JavaScript, Java, C++, C#, Go, Rust, PHP, Ruby, etc.
- **Web:** HTML, CSS, SCSS, Vue, React, Angular, etc.
- **Données:** JSON, XML, YAML, CSV, SQL, etc.
- **Documents:** PDF, DOCX, XLSX, PPTX, Markdown, TXT, etc.
- **Configuration:** INI, CONF, ENV, Properties, etc.
- **Archives:** ZIP, RAR, 7Z, TAR, GZ, etc.

Liste complète: [SUPPORTED_FILE_TYPES.md](../SUPPORTED_FILE_TYPES.md)

### Q: Ai-je besoin d'Internet pour Master Search?

**R:** Non!
- ✅ Entièrement fonctionnel hors ligne
- ✅ Aucune transmission de données
- ✅ Confidentialité garantie
- ℹ️ La mise à jour du navigateur pour les rapports HTML est optionnelle

---

## Dépannage

### Problème: La recherche est très lente

**Solutions:**
1. Choisir un répertoire plus étroit
   - Au lieu de `C:\` → `C:\Projects\`
2. Utiliser un filtre de type de fichier
   - Au lieu de "Tous" → "Code"
3. Désactiver "Chercher dans les fichiers"
   - Si vous avez seulement besoin de noms de fichiers
4. Utiliser des termes de recherche plus spécifiques
   - `main.py` au lieu de `main`

### Problème: Erreur "Accès refusé"

**Causes et solutions:**
1. Des droits d'administrateur sont nécessaires
   - Ouvrir l'interface avec un clic droit → "Exécuter en tant qu'administrateur"
2. Fichier en cours d'utilisation
   - Fermer les autres programmes
3. L'antivirus bloque l'accès
   - Ajouter Master Search à la liste blanche

### Problème: Le rapport ne s'ouvre pas

**Solutions:**
1. Vérifier les paramètres du navigateur
   - Permettre l'ouverture de fichiers locaux?
2. Désactiver le bloqueur de fenêtres contextuelles
   - Le rapport s'ouvre dans un nouvel onglet
3. Changer le navigateur par défaut
   - Modifier dans les paramètres Windows
4. Ouvrir le fichier HTML manuellement
   - Ouvrir le dossier Rapports, double-cliquer sur le fichier HTML

### Problème: Certains types de fichiers sont ignorés

**Causes:**
1. Le filtre de type de fichier est trop restrictif
   - Mettre sur "Tous"
2. L'extension de fichier n'est pas dans la liste blanche
   - Voir SUPPORTED_FILE_TYPES.md pour plus de détails

### Problème: L'expression régulière ne fonctionne pas

**Erreurs courantes:**
1. L'option d'expression régulière n'est pas activée
   - ☑️ Case à cocher "Expressions régulières"
2. Erreur de syntaxe dans l'expression régulière
   - Trop de `(` sans fermeture
   - Séquences d'échappement invalides
3. Variations de motif
   - `\d` dans les chaînes brutes ✅
   - `\\d` (double antislash) aussi possible

**Outils de test:**
- [regex101.com](https://regex101.com) - Testeur d'expressions régulières en ligne
- Testez le motif là avant de l'utiliser dans Master Search

### Problème: Master Search ne répond pas

**Solutions:**
1. Annuler la recherche
   - Cliquer sur le bouton [ANNULER]
2. Fermer avec Ctrl+Z
3. Redémarrer
   - Devrait prendre 1-2 secondes normalement

---

## Sujets avancés

### Interface de ligne de commande (CLI)

Master Search peut également être utilisé depuis la ligne de commande:

```powershell
# Recherche de base
python cli_main.py --search test --path C:\Projects

# Avec options
python cli_main.py --search main --path C:\src --in-files --regex

# Générer un rapport
python cli_main.py --search TODO --path . --report

# Toutes les options
python cli_main.py --help
```

### Intégration avec d'autres outils

**Exemple: Tuyauterie PowerShell**
```powershell
# Recherche + Traitement des rapports
master_search.exe --search error --path C:\Logs | Process-SearchResults
```

**Exemple: Planificateur Windows**
```
Tâche planifiée → Master Search → quotidiennement à 22:00
Le rapport est généré automatiquement et envoyé par e-mail
```

---

## Support et contact

**Problèmes trouvés?**
- 📧 Email: info@loony-tech.de
- 🐛 Rapport de bogue: [GitHub Issues](https://github.com/Loony2392/master-search)
- 💬 Questions: Forum communautaire (à venir)

**Informations sur la version:**
- **Version actuelle:** 2025.11.7
- **Dernière mise à jour:** 12 novembre 2025
- **Auteur:** Loony2392
- **Licence:** Propriétaire

---

## Licence et conditions légales

Master Search™ - Outil professionnel de recherche de fichiers
© 2025 Loony2392 & LOONY-TECH. Tous droits réservés.

**Confidentialité:**
- ✅ Aucune collecte de données
- ✅ Aucune télémétrie
- ✅ Entièrement hors ligne
- ✅ Traitement local uniquement

---

**Bonne recherche! 🚀**

*Master Search - Recherche professionnelle de fichiers avec beaux rapports*
