def calcular_tiempo_total():
    total_minutos = 0

    while True:
        tiempo_tramo = int(input("Ingrese el tiempo del tramo (en minutos), o 0 para terminar: "))

        if tiempo_tramo == 0:
            break

        total_minutos += tiempo_tramo

    horas = total_minutos // 60
    minutos = total_minutos % 60

    print(f"El tiempo total del viaje es: {horas} horas y {minutos} minutos.")

if __name__ == "__main__":
    calcular_tiempo_total()
