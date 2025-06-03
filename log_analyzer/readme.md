# 🕵️‍♂️ Log Analyzer- CYBERSEC

██╗      ██████╗  ██████╗      █████╗ ███╗   ██╗ █████╗ ██╗  ██╗███████╗██████╗ 
██║     ██╔═══██╗██╔════╝     ██╔══██╗████╗  ██║██╔══██╗██║ ██╔╝██╔════╝██╔══██╗
██║     ██║   ██║██║  ███╗    ███████║██╔██╗ ██║███████║█████╔╝ █████╗  ██████╔╝
██║     ██║   ██║██║   ██║    ██╔══██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  ██╔══██╗
███████╗╚██████╔╝╚██████╔╝    ██║  ██║██║ ████║██║  ██║██║  ██╗███████╗██║  ██║
╚══════╝ ╚═════╝  ╚═════╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═

Une application Python interactive pour analyser les fichiers de logs serveurs (Apache, Nginx, SSH) et détecter des comportements suspects.

---

## 🎯 Objectifs pédagogiques

- Lire et analyser des fichiers de logs système ou web.
- Détecter des signes d’attaque (brute-force, accès 403, scans).
- Manipuler les expressions régulières (regex).
- Générer un rapport automatisé.
- Créer une interface graphique (Tkinter) avec style "hacker".

---

## 🗂️ Structure du projet

log-analyzer/
├── logs/
│ └── access.log # Fichier log à analyser
├── analyzer.py # Script principal avec interface Tkinter
├── utils.py # Fonctions de parsing et détection
├── report.txt # Rapport généré
└── README.md # Ce fichier


---

## 🚀 Lancement

### Interface graphique (Tkinter)
```bash
python analyzer.py

