import RPi.GPIO as GPIO
import time

# Configuración de pines
TRIG_PIN = 23
ECHO_PIN = 24

def setup():
    # Configuración de los pines
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)

def get_distance():
    # Envía un pulso corto para activar el sensor
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Espera a que el sensor responda
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Calcula la duración del pulso y calcula la distancia
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150  # La velocidad del sonido es aproximadamente 343 metros/segundo

    return round(distance, 2)

def cleanup():
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        setup()

        while True:
            distance = get_distance()
            print(f"Distancia: {distance} cm")
            time.sleep(1)

    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
    finally:
        cleanup()
