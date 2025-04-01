# Ransomware Light (Simulation Pédagogique)

⚠️ **Avertissement**  
Ce script est un outil **à but pédagogique uniquement**, conçu pour simuler le comportement d’un ransomware dans un **environnement Linux isolé** (machine virtuelle, laboratoire fermé).  
**Ne l’exécutez jamais sur un système réel, personnel ou professionnel.**

---

## 🎯 Objectif

Simuler un ransomware capable de :
- Générer une clé de chiffrement symétrique (XOR)
- Chiffrer tous les fichiers accessibles sur `/`
- Exfiltrer la clé vers un serveur distant via `curl`
- Créer un message de rançon fictif dans `/root`
- Redémarrer la machine

---

## 📁 Fichiers

| Fichier | Description |
|--------|-------------|
| `ransomware_light.py` | Script principal du ransomware |
| `README.md` | Ce fichier d'instructions |

---

## ⚙️ Fonctionnement

1. Génère une clé simple (XOR sur 1 octet)
2. Stocke temporairement la clé dans `/tmp/ransom_key.txt`
3. Exfiltre la clé vers un serveur HTTP (modifiez l'URL dans le script)
4. Chiffre tous les fichiers modifiables accessibles via `os.walk('/')`
5. Écrit une note de rançon simulée dans `/root/README.txt`
6. Redémarre le système automatiquement après 5 secondes
