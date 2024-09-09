def clasificar_leucemia():
    pacientes = 803  # Número de pacientes
    clasificaciones = []
    
    for i in range(1, pacientes + 1):
        puntaje = int(input(f"Ingrese el puntaje de Leucemia del paciente {i}: "))
        if puntaje < 10:
            nivel = "No tiene Leucemia"
        elif 11 <= puntaje <= 40:
            nivel = "Nivel bajo de Leucemia"
        elif 41 <= puntaje <= 69:
            nivel = "Nivel moderado de Leucemia"
        elif 70 <= puntaje <= 100:
            nivel = "Nivel grave de Leucemia"
        else:
            nivel = "Puntaje no válido"
        
        clasificaciones.append((i, puntaje, nivel))  # Se guarda la clasificación en una lista
    
    return clasificaciones

resultados = clasificar_leucemia()
for paciente in resultados:
    print(f"Paciente {paciente[0]}: Puntaje: {paciente[1]}, Clasificación: {paciente[2]}")
