from machine import Pin, PWM
import time

# Configuration du GPIO pour l'émission
gpio_pin = Pin(1, Pin.OUT)  # GPIO 1 en sortie
pwm = PWM(gpio_pin)  # Activation du signal PWM

# Fréquence de la porteuse
FREQ = 1000  # 1 kHz

# Fonction pour envoyer un bit
def send_bit(bit):
    if bit == 1:
        pwm.freq(FREQ)  # Générer PWM à 1 kHz
        pwm.duty_u16(32768)  # Rapport cyclique 50% (32768/65535)
    else:
        pwm.duty_u16(0)  # Signal OFF pour bit 0
    time.sleep(0.001)  # Durée de 1 ms par bit (1 kHz)

# Fonction pour envoyer une trame hexadécimale
def send_frame(hex_data):
    print("Envoi de la trame...")
    for byte in hex_data:
        binary_string = bin(byte)[2:].zfill(8)  # Convertir en binaire (8 bits)
        print(f"Envoi de l'octet {byte:02X} -> {binary_string}")
        for bit in binary_string:
            send_bit(int(bit))  # Envoyer chaque bit
    # Fin de la transmission
    pwm.duty_u16(0)  # Désactiver le signal PWM
    print("Trame envoyée.")

# Fonction principale
def main():
    # Exemple de trame à envoyer : "48656C6C6F" => "Hello" en ASCII
    data_to_send = "48656C6C6F"  # Trame en hexadécimal
    hex_data = [int(data_to_send[i:i+2], 16) for i in range(0, len(data_to_send), 2)]
    
    try:
        while True:
            send_frame(hex_data)  # Envoyer la trame
            time.sleep(2)  # Attendre 2 secondes avant la prochaine émission
    except KeyboardInterrupt:
        pwm.duty_u16(0)  # Arrêter proprement le signal PWM
        print("Émission arrêtée.")

# Lancer le programme principal
main()