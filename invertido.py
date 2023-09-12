def es_palindromo(numero):
    original = numero
    invertido = 0

    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero //= 10

    return original == invertido

# Solicitar al usuario que ingrese un número natural
numero = int(input("Ingrese un número natural: "))

if es_palindromo(numero):
    print(f"{numero} es un palíndromo.")
else:
    print(f"{numero} no es un palíndromo.")
