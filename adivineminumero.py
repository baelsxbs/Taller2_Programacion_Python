def adivina_mi_numero():
    print("Piensa en un número entre 1 y 100 y yo trataré de adivinarlo.")
    print("Después de cada intento, ingresa < si es menor, > si es mayor o = si adiviné.")
    input("Presiona Enter cuando estés listo para comenzar...")

    min_numero = 1
    max_numero = 100

    while True:
        intento = (min_numero + max_numero) // 2
        print(f"¿Es {intento} tu número? (<, >, =): ")
        respuesta = input()

        if respuesta == ">":
            min_numero = intento + 1
        elif respuesta == "<":
            max_numero = intento - 1
        elif respuesta == "=":
            print(" He adivinado tu número.")
            break
        else:
            print("Por favor, ingresa <, > o =.")

adivina_mi_numero()
