# utils.py
import re
from collections import defaultdict

def parse_ligne(log_line):
    pattern = (r'(?P<ip>\d+\.\d+\.\d+\.\d+) - - '
               r'\[(?P<datetime>[^\]]+)\] '
               r'"(?P<method>\S+) (?P<url>\S+) (?P<protocol>\S+)" '
               r'(?P<code>\d{3}) (?P<size>\d+)')
    match = re.match(pattern, log_line)
    if match:
        print(f"[INFO] Ligne parsée : {match.groupdict()}")
    else:
        print(f"[WARN] Ligne non reconnue : {log_line.strip()}")
    return match.groupdict() if match else None

def detecte_suspect(donnees):
    code = donnees.get("code")
    url = donnees.get("url")

    if code == "403":
        print(f"[ALERTE] 403 détecté pour {donnees['ip']} sur {url}")
        return True
    if code == "404" and url.startswith("/admin"):
        print(f"[ALERTE] Tentative d'accès à /admin avec 404 par {donnees['ip']}")
        return True
    if "/login" in url and code.startswith("4"):
        print(f"[ALERTE] Tentative d'échec login par {donnees['ip']} (code {code})")
        return True
    return False

def generer_rapport(liste_donnees, chemin):
    compte_par_ip = defaultdict(int)
    for ligne in liste_donnees:
        ip = ligne.get("ip")
        source = ligne.get("source", "inconnu")
        compte_par_ip[(ip, source)] += 1

    with open(chemin, "w", encoding="utf-8") as f:
        for (ip, source), count in compte_par_ip.items():
            f.write(f"[{source.upper()}] {ip} a déclenché {count} comportements suspects\n")