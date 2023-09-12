def grafico_valores():
    valores_positivos = 0
    valores_negativos = 0

    while True:
        valor = int(input("Ingrese un valor entero (0 para salir): "))

        if valor > 0:
            valores_positivos += 1
        elif valor < 0:
            valores_negativos += 1
        elif valor == 0:
            break

    print("Gráfico:")
    print("*" * valores_positivos + " (Valores positivos)")
    print("*" * valores_negativos + " (Valores negativos)")

# Llamamos a la función para ejecutar el programa
grafico_valores()
