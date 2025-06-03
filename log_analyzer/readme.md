# 🕵️ Log Analyzer - CYBERSEC

Une application Python interactive pour analyser les fichiers de logs serveurs (Apache, Nginx, SSH) et détecter des comportements suspects. Inclut une intelligence artificielle de détection d'anomalies basée sur Isolation Forest.

---

## 🎯 Objectifs

- Lire et analyser des fichiers de logs système ou web
- Détecter des comportements suspects via règles ou IA
- Manipuler des expressions régulières (regex)
- Créer un rapport automatique et interprétable

---

## 🧠 Fonctionnement

L'analyseur fonctionne en 2 modes :

1. **Règles manuelles (basées sur des codes HTTP connus)**
   - 403 : accès interdit
   - 404 + /admin : tentative de scan
   - /login + 4xx : brute-force

2. **IA avec Isolation Forest**
   - Entraînée localement sur le fichier log
   - Détecte les lignes "anormales" sans les connaître à l'avance

---

## 📂 Structure du projet
```
log-analyzer/
├── logs/
│   └── access.log         # Exemple de log à analyser
├── analyzer.py            # Interface graphique principale
├── utils.py               # Fonctions de parsing et rapport
├── ai_model.py            # IA Isolation Forest + vectoriseur
├── log_model.pkl          # Modèle IA sauvegardé
├── vectorizer.pkl         # TF-IDF vectoriseur sauvegardé
├── report.txt             # Résultat de l'analyse
└── README.md              # Ce fichier
```

---

## 🚀 Lancement

```bash
python analyzer.py
```

- Utilise une interface graphique (Tkinter)
- Choisis ton fichier log
- Active/désactive l'IA
- Lance l’analyse et observe les résultats

---

## 📝 Exemple de sortie

```
[RULE] 192.168.1.10 a déclenché 2 comportements suspects
[IA]   192.168.1.20 a déclenché 1 comportements suspects
```

---

## 📦 Prérequis

- Python ≥ 3.10
- `scikit-learn`
- `joblib`

```bash
pip install scikit-learn joblib
```

---

## 📚 À retenir

- Les fichiers `.pkl` permettent de **sauvegarder l’intelligence du modèle**
- Tu peux comparer les détections `[RULE]` vs `[IA]`
- L’IA est **non supervisée** et apprend directement à partir du fichier log

---

## 👨‍💻 Auteur
Projet créé par [09prodige](https://github.com/09prodige) pour apprendre à intégrer des techniques d'IA simples dans des outils de cybersécurité.

