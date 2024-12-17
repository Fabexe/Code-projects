from machine import Pin, Timer
import time

# Configuration du GPIO pour l'entrée du signal
gpio_pin = Pin(1, Pin.IN, Pin.PULL_DOWN)  # GPIO 1 en entrée

# Paramètres de réception
BIT_DURATION = 0.0001  # Durée de chaque bit : 0.1 ms
bitstream = []  # Liste pour stocker les bits reçus
nibbles_received = []  # Liste pour stocker les trames de 4 bits

# Fonction pour lire un bit
def read_bit(timer):
    global bitstream
    value = gpio_pin.value()  # Lire l'état actuel du GPIO (0 ou 1)
    bitstream.append(value)  # Ajouter le bit lu à la liste
    
    # Accumuler les bits par groupes de 4 pour former un nibble
    if len(bitstream) == 4:
        nibble = int("".join(map(str, bitstream)), 2)  # Convertir les 4 bits en entier (base 2)
        nibbles_received.append(nibble)
        bitstream.clear()  # Réinitialiser les bits pour le prochain groupe

# Configuration de la minuterie pour échantillonner le signal à intervalles réguliers (10 kHz)
sampling_timer = Timer()
sampling_timer.init(freq=10000, mode=Timer.PERIODIC, callback=read_bit)  # Échantillonnage à 10 kHz (0.1 ms/bit)

# Fonction principale
def main():
    print("Attente de la réception des trames de 4 bits...")
    try:
        while True:
            if nibbles_received:
                # Afficher les trames reçues en Hexadécimal
                hex_data = ' '.join(['{:X}'.format(nibble) for nibble in nibbles_received])
                print(f"Trames reçues (4 bits Hex) : {hex_data}")
                
                # Réinitialiser les nibbles reçus après l'affichage
                nibbles_received.clear()
            time.sleep(0.1)  # Pause légère pour éviter une surcharge du processeur
    except KeyboardInterrupt:
        print("Réception arrêtée.")
        sampling_timer.deinit()  # Désactiver proprement la minuterie

# Lancer le programme principal
main()