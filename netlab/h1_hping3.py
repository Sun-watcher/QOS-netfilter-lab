
#!/usr/bin/python3

import subprocess, sys

dport = "5001"
TOS = "10"
dest_ip = "192.168.20.1"
ttl = "3"
arguments = [dport, TOS, dest_ip, ttl]

for i in range(1, len(sys.argv)):
	arguments[i-1] = sys.argv[i]


commande = f"hping3 -c 1 -V -A   --destport {arguments[0]} --tos {arguments[1]} --ttl {ttl} {arguments[2]}"
print(commande)
envoie_ping = subprocess.Popen(commande, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)

print("dport : ",arguments[0], ", ToS : ", arguments[1], ", dest_ip : ", arguments[2], ",ttl :", arguments[3])
stdout, stderr = envoie_ping.communicate()

print(stderr.decode())
print(stdout.decode())


