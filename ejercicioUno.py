def calcular_serie():
    serie = []
    a, b = 5, 8
    while len(serie) < 100:
        if a != 13:
            serie.append(a)
        a, b = b, a + b
    return serie

resultado = calcular_serie()
print(resultado)
