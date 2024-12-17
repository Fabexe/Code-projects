from machine import Pin, PWM
import time

# Configuration du GPIO pour l'émission
gpio_pin = Pin(0, Pin.OUT)  # GPIO 0 en sortie
pwm = PWM(gpio_pin)  # Activation du signal PWM

# Paramètres d'émission
FREQ = 1000  # Fréquence de 1 kHz
BIT_DURATION = 0.0001  # 0.1 ms par bit

# Fonction pour envoyer un bit
def send_bit(bit):
    if bit == 1:
        pwm.freq(FREQ)  # Configurer la fréquence à 1 kHz
        pwm.duty_u16(32768)  # Rapport cyclique de 50% (32768/65535)
    else:
        pwm.duty_u16(0)  # Pas de signal pour bit 0
    time.sleep(BIT_DURATION)  # Durée de 0.1 ms par bit

# Fonction pour envoyer une trame de 4 bits
def send_nibble(nibble):
    binary_string = bin(nibble)[2:].zfill(4)  # Convertir en binaire (4 bits)
    print(f"Envoi des 4 bits : {binary_string}")
    for bit in binary_string:
        send_bit(int(bit))  # Envoyer chaque bit
    pwm.duty_u16(0)  # Désactiver le signal PWM après la trame

# Fonction principale
def main():
    # Exemple de trame : liste de nibbles (4 bits chacun)
    data_to_send = [0b1010, 0b0101, 0b1111, 0b0000]  # Exemple : 4 nibbles (A, 5, F, 0)
    
    try:
        while True:
            print("Début de l'émission...")
            for nibble in data_to_send:
                send_nibble(nibble)  # Envoyer chaque trame de 4 bits
                time.sleep(0.001)  # Pause de 1 ms entre les trames pour éviter un chevauchement
            print("Trame envoyée. Attente avant réémission...")
            time.sleep(2)  # Attente de 2 secondes avant la prochaine émission
    except KeyboardInterrupt:
        pwm.duty_u16(0)  # Arrêter proprement le signal PWM
        print("Émission arrêtée.")

# Lancer le programme principal
main()