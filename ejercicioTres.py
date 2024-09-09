def contar_pares_impares():
    numeros = []
    pares = 0
    impares = 0
    
    for i in range(400):  # Se repite 400 veces
        numero = int(input(f"Ingrese el número {i+1}: "))
        numeros.append(numero)
        if numero % 2 == 0:  # Si el número es divisible por 2, es par
            pares += 1
        else:  # Si no, es impar
            impares += 1
    
    return numeros, pares, impares

numeros, pares, impares = contar_pares_impares()
print("Listado de números:", numeros)
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
