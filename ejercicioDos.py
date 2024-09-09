def calcular_salarios():
    empleados = 1897  # Número total de empleados
    listado_empleados = []
    
    for i in range(1, empleados + 1):  # Para cada empleado
        salario_base = float(input(f"Ingrese el salario base del empleado {i}: "))
        comisiones = float(input(f"Ingrese las comisiones del empleado {i}: "))
        seguridad_social = salario_base * 0.08  # Deducción del 8% para seguridad social
        salario_total = salario_base + comisiones - seguridad_social  # Cálculo del salario total
        listado_empleados.append((i, salario_base, comisiones, seguridad_social, salario_total))
    
    return listado_empleados

salarios = calcular_salarios()
for empleado in salarios:
    print(f"Empleado {empleado[0]}: Salario Base: {empleado[1]}, Comisiones: {empleado[2]}, Seguridad Social: {empleado[3]}, Salario Total: {empleado[4]}")

"""Segunda forma de realizar el ejercicio definiendo como dato general el salario base y la comision para todos los empleados"""
def calcular_salarios_generales():
    empleados = 1897  # Número total de empleados
    salario_base = 1300000  # Salario base fijo para todos los empleados
    comisiones = 150000  # Comisiones fijas para todos los empleados
    listado_empleados = []

    for i in range(1, empleados + 1):  # Para cada empleado
        seguridad_social = salario_base * 0.08  # Deducción del 8% para seguridad social
        salario_total = salario_base + comisiones - seguridad_social  # Cálculo del salario total
        listado_empleados.append((i, salario_base, comisiones, seguridad_social, salario_total))
    
    return listado_empleados

# Mostramos los salarios calculados
salarios = calcular_salarios_generales()
for empleado in salarios:
    print(f"Empleado {empleado[0]}: Salario Base: {empleado[1]}, Comisiones: {empleado[2]}, Seguridad Social: {empleado[3]}, Salario Total: {empleado[4]}")