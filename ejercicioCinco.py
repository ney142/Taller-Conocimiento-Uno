def clasificar_cabinas():
    cabinas = 407  # Número de cabinas
    clasificaciones = []
    
    for i in range(1, cabinas + 1):
        puntaje = int(input(f"Ingrese el puntaje de la cabina {i}: "))
        if puntaje == 2:
            clasificacion = "Funcionamiento defectuoso"
        elif puntaje == 3:
            clasificacion = "Funcionamiento moderado"
        elif puntaje == 4:
            clasificacion = "Funcionamiento óptimo"
        else:
            clasificacion = "Puntaje no válido"
        
        clasificaciones.append((i, puntaje, clasificacion))
    
    return clasificaciones

resultados = clasificar_cabinas()
for cabina in resultados:
    print(f"Cabina {cabina[0]}: Puntaje: {cabina[1]}, Clasificación: {cabina[2]}")
