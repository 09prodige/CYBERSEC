"""Auteur : AKWE EYI Jérémie
   Date: 03/06/2025
   Objectif : Appel des fonctions nécessaires pour analyser des logs
"""

# utils.py
import re
from collections import defaultdict

def parse_ligne(log_line):
    # Regex pour logs Apache/Nginx standards
    pattern = (r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - '  # IP
               r'\[(?P<datetime>[^\]]+)\] '            # Date
               r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" '  # Requête
               r'(?P<code>\d{3}) (?P<size>\d+)')        # Code HTTP et taille

    match = re.match(pattern, log_line)
    if not match:
        return None

    return match.groupdict()


def detecte_suspect(donnees):
    code = donnees.get("code")
    url = donnees.get("url")

    # Règles : accès interdit, scanning ou brute-force (simulé par accès répétitif au login)
    if code == "403":
        return True
    if code == "404" and url.startswith("/admin"):
        return True
    if "/login" in url and code.startswith("4"):
        return True

    return False


def generer_rapport(liste_donnees, chemin):
    compte_par_ip = defaultdict(int)

    for ligne in liste_donnees:
        ip = ligne.get("ip")
        compte_par_ip[ip] += 1

    with open(chemin, "w") as f:
        for ip, count in compte_par_ip.items():
            f.write(f"[ALERTE] {ip} a déclenché {count} comportements suspects\n")