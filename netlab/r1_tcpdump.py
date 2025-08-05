#!/usr/bin/python3
import subprocess
interface_reseau = "r1-eth0"
filtre_ecoute = f"'ip and (ip[1] & 0x10 == 0x10)'"
commande = f"tcpdump -c 1 -ln -i {interface_reseau} "
ecoute_reseau = subprocess.Popen((commande + filtre_ecoute).encode(),shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

while True:
	ligne = ecoute_reseau.stdout.read() 
	if(ligne):
		print("Résultat du TCPDUMP :", ligne)
		break
