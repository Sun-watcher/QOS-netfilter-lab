#!/usr/bin/python3
import subprocess, threading, sys

# Intercepter le paquet
interface_reseau = "r1-eth0"
filtre_TOS_01 = "'ip and (ip[1] & 0x01 == 0x01)'"
filtre_TOS_02 = "'ip and (ip[1] & 0x02 == 0x02)'"
filtre_TOS_04 = "'ip and (ip[1] & 0x04 == 0x04)'"

commande = f"tcpdump -c 1 -v -ln -i {interface_reseau} "

# Marquer les paquets avec le firewall
commande_marquage_TOS_01 = "sudo iptables -t mangle -A PREROUTING -j TOS --set-tos 0x01"
commande_marquage_TOS_02 = "sudo iptables -t mangle -A PREROUTING -j TOS --set-tos 0x02"
commande_marquage_TOS_04 = "sudo iptables -t mangle -A PREROUTING -j TOS --set-tos 0x04"

event = threading.Event()

def ecouter_reseau(filtre):
	commande = f"tcpdump -c 1 -ln -i {interface_reseau} "
	commande = commande + filtre
	process = subprocess.Popen(commande.encode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	if(stdout):
		if(filtre == filtre_TOS_01):
			print("Marquage TOS 0x01")
			subprocess.Popen(commande_marquage_TOS_01, shell = True)
		elif(filtre == filtre_TOS_02):
			print("Marquage TOS 0x02")
			subprocess.Popen(commande_marquage_TOS_02, shell = True)
		elif(filtre == filtre_TOS_04):
			print("Marquage TOS 0x04")
			subprocess.Popen(commande_marquage_TOS_04, shell = True)
		event.set()
		sys.exit(1)
def fin_thread():
	event.wait()

thread_TOS_01 = threading.Thread(target=ecouter_reseau, args=(filtre_TOS_01,))
thread_TOS_02 = threading.Thread(target=ecouter_reseau, args=(filtre_TOS_02,))
thread_TOS_04 = threading.Thread(target=ecouter_reseau, args=(filtre_TOS_04,))
thread_fin = threading.Thread(target=fin_thread)

thread_TOS_01.start()
thread_TOS_02.start()
thread_TOS_04.start()
thread_fin.start()

thread_fin.join()
