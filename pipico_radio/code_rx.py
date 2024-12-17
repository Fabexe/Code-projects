from machine import Pin, Timer
import time

# Configuration du GPIO pour l'entrée du signal
gpio_pin = Pin(1, Pin.IN, Pin.PULL_DOWN)

# Variables globales
bitstream = []  # Pour stocker les bits reçus
byte_received = []  # Pour stocker les octets reconstruits

# Fonction pour détecter un bit sur front descendant
def read_bit(pin):
    global bitstream
    value = pin.value()  # Lire l'état actuel du pin (1 ou 0)
    bitstream.append(value)
    
    # On accumule les bits par groupes de 8 pour former un octet
    if len(bitstream) == 4:
        byte = int("".join(map(str, bitstream)), 2)  # Convertir les bits en un entier
        byte_received.append(byte)
        bitstream.clear()  # Réinitialiser les bits pour le prochain octet

# Configuration d'une minuterie pour échantillonner le signal à 1 kHz
sampling_timer = Timer()
sampling_timer.init(freq=1000, mode=Timer.PERIODIC, callback=lambda t: read_bit(gpio_pin))

# Fonction principale
def main():
    print("Attente de la réception de données...")
    try:
        while True:
            if byte_received:
                # Afficher les données reçues en ASCII
                hex_data = ''.join(['{:X}'.format(b) for b in byte_received])
                ascii_data = ''.join([chr(b) for b in byte_received if 32 <= b <= 126])  # Filtre ASCII imprimable
                print(f"Données reçues (Hex) : {hex_data}")
                print(f"Données reçues (ASCII) : {ascii_data}")
                byte_received.clear()
            time.sleep(0.0001)
    except KeyboardInterrupt:
        print("Programme arrêté.")
        sampling_timer.deinit()  # Désactiver la minuterie

# Lancer le programme principal
main()