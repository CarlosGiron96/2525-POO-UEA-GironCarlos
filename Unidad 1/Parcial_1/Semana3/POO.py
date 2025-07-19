#Se define una funcion donde se realice el calculo de promedio
def calcular_promedio_semanal_clima(temperaturas_semanales):
#Se valida que exisgtan valores de lo cuales hacer el calculo
  if not temperaturas_semanales:
    return None  # No hay temperaturas para calcular la media

  suma_temperaturas = sum(temperaturas_semanales)
  numero_de_dias = len(temperaturas_semanales)
  promedio_semanal = suma_temperaturas / numero_de_dias
  return promedio_semanal

# Se definen datos de las temperaturas
temperaturas = [25, 26, 27, 28, 29, 25, 24]
#Se llama a la funcion que hace el calculo de promedio
promedio = calcular_promedio_semanal_clima(temperaturas)
#Se muestra un mensaje con los datos de promedio
if promedio is not None:
  print(f"La temperatura promedio de la semana es: {promedio:.2f} °C")
else:
  print("No hay datos de temperatura para calcular el promedio.")