#Un empleado fue contratado durante un periodo específico en días y por un salario,
#ambos conocidos e ingresados desde teclado. Construya un programa que permita
#calcular el valor de su liquidación al terminar el contrato. La liquidación se compone de
#prima, cesantías, intereses a las cesantías y vacaciones. Para calcular estos valores,
#se usan las siguientes formulas:
#• Prima: salario x días laborados / 360
#• Cesantías: salario x días laborados / 360
#• Intereses cesantías: cesantías x 12% / días laborados
#• Vacaciones: salario x días laborados / 720


#Desarrolo



# Definir las funciones para calcular los valores de la liquidación
def calcular_prima(salario, dias_laborados):
    return salario * dias_laborados / 360

def calcular_cesantias(salario, dias_laborados):
    return salario * dias_laborados / 360

def calcular_intereses_cesantias(cesantias, dias_laborados):
    return cesantias * 0.12 / dias_laborados

def calcular_vacaciones(salario, dias_laborados):
    return salario * dias_laborados / 720

# Pedir los datos de entrada al usuario
nombre = input("Ingrese su nombre: ")
dias_laborados = int(input("Ingrese los días laborados: "))
salario = float(input("Ingrese su salario: "))

# Calcular los valores de la liquidación
prima = calcular_prima(salario, dias_laborados)
cesantias = calcular_cesantias(salario, dias_laborados)
intereses_cesantias = calcular_intereses_cesantias(cesantias, dias_laborados)
vacaciones = calcular_vacaciones(salario, dias_laborados)
liquidacion = prima + cesantias + intereses_cesantias + vacaciones

# Mostrar los resultados
print(f"Señor {nombre} para los {dias_laborados} días laborados y salario ${salario:.2f}, su liquidación se compone así:")
print(f"Prima: ${prima:.2f}")
print(f"Cesantía: ${cesantias:.2f}")
print(f"Intereses cesantías: ${intereses_cesantias:.2f}")
print(f"Vacaciones: ${vacaciones:.2f}")
print(f"Liquidación: ${liquidacion:.2f}")