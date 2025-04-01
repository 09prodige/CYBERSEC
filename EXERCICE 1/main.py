"""
Auteur: Jeremie AKWE
Date: 31/03/2025
EXERCICE 1 :
 1-Utiliser la fonction input pour
récupérer l'ip fournit par un user
2- Executer une commande ping depuis python
3- Vérifier si la cible repond ou non
4- Utiliser "SubProcess" pour manipuler les commandes Shell
5- Use if - else
6- Contrainte : Doit fonctionner sur Windows/Linux, et gérer les erreurs
propres au système
-
"""
import subprocess
import platform

ip = input("Veuillez entrer une adresse ip:")

#Detecter l'OS  pour adapter la commande

param = "-n" if platform.system().lower() == "windows" else "-c"
commande = ["ping", param, "1", ip]


print("Ping en cours")

#Executer ping

#Stocker le resultat
result = subprocess.run(commande, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

try:

    if result.returncode == 0:
        print("Cible en ligne")
    else:
        print("La cible n'est pas en ligne")
except Exception as e:
    print(f"Erreur lors du ping{e}")
