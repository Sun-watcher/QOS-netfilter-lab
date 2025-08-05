#!/usr/bin/python3

import socket
import struct

def forge_arp_request(src_mac, src_ip, target_ip, interface):
    # Convertir les adresses IP en format binaire
    src_ip_bytes = socket.inet_aton(src_ip)
    target_ip_bytes = socket.inet_aton(target_ip)
    
    # Convertir l'adresse MAC en binaire
    src_mac_bytes = bytes.fromhex(src_mac.replace(':', ''))
    broadcast_mac = b'\xff\xff\xff\xff\xff\xff'  # Adresse MAC de diffusion
    
    # Construire l'en-tête Ethernet
    eth_header = struct.pack('!6s6sH', broadcast_mac, src_mac_bytes, 0x0806)
    
    # Construire le paquet ARP
    hardware_type = 1  # Ethernet
    protocol_type = 0x0800  # IPv4
    hardware_size = 6  # Taille de l'adresse MAC
    protocol_size = 4  # Taille de l'adresse IP
    opcode = 1  # Requête ARP
    arp_request = struct.pack(
        '!HHBBH6s4s6s4s',
        hardware_type,
        protocol_type,
        hardware_size,
        protocol_size,
        opcode,
        src_mac_bytes,
        src_ip_bytes,
        b'\x00\x00\x00\x00\x00\x00',  # Adresse MAC cible (inconnue)
        target_ip_bytes
    )
    
    # Construire la trame complète
    return eth_header + arp_request

def send_arp_request(interface, frame):
    # Créer une socket Raw avec le protocole Ethernet
    sock = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0806))
    sock.bind((interface, 0))
    sock.send(frame)
    sock.close()

src_mac = "00:11:22:33:44:55"  # Remplacez par l'adresse MAC de h3
src_ip = "192.168.1.3"         # Remplacez par l'adresse IP de h3
target_ip = "192.168.1.1"      # Remplacez par l'adresse IP de h1
interface = "eth0"             # Interface réseau sur laquelle envoyer la trame

# Forger et envoyer la requête ARP
frame = forge_arp_request(src_mac, src_ip, target_ip, interface)
send_arp_request(interface, frame)
print("Requête ARP envoyée avec succès.")
