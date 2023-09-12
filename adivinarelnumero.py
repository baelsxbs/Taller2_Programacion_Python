import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intentos += 1
        intento_usuario = int(input(f"Intento #{intentos}: "))

        if intento_usuario < numero_secreto:
            print("El número pensado es mayor.")
        elif intento_usuario > numero_secreto:
            print("El número pensado es menor.")
        else:
            print(f"¡Correcto! ¡Has adivinado el número en {intentos} intentos!")
            break

adivina_el_numero()
