#Scanner de port
import threading
from socket import socket


#Definir une fonction qui va tester un sport spécifique
def scan_port(host, port):

    try:
        #Création d'un socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Delai pour éviter des erreurs
        sock.settimeout(1)

        #Tentative de connexion sur le port (0 si la connexion a reussi)
        result = sock.connect_ex((host, port))
        #Si le port est ouvert (result == 0), on l'affiche
        if result == 0:
            print (f"[+] Port {port} is open")
        #On ferme le socket
        sock.close()
    except Exception as e:
        #Gestion des erreurs
        print(f"[-] Erreur sur le port {port}: {e}")

#Adresse ip de la cible
target = input("Entrez l'ip à scanner")

#Plage d'adresse à scanner
start_port = int(input("Port de début"))
end_port = int(input("Port de fin"))

#Début de scan
print(f"\n[***] scan target {target} sur les ports {start_port}-{end_port}[***]")
for port in range(start_port, end_port+1):
    #Thread (execution parallèle) pour chaque port
    t = threading.Thread(target=scan_port, args=(target, port))


