#Primero se ingresan las temperaturas de toda la semana en una lista
lunes = int(input("Ingrese la temperatura del dia lunes: "))
martes=int(input("Ingrese la temperatura del dia martes: "))
miercoles=int(input("Ingrese la temperatura del dia miercoles: "))
jueves=int(input("Ingrese la temperatura del dia jueves: "))
viernes=int(input("Ingrese la temperatura del dia viernes: "))
sabado=int(input("Ingrese la temperatura del dia sabado: "))
domingo=int(input("Ingrese la temperatura del dia domingo: "))
#Se ordena los datos ingresados en un lista
temperaturas = [lunes,martes,miercoles,jueves,viernes,sabado,domingo]
#se valida que la lista no este vacia
if len(temperaturas) >0 :
  #Se realice los calculos del promedio
    suma_temperaturas = sum(temperaturas)
    numero_de_dias = len(temperaturas)
    promedio_semanal = float(suma_temperaturas / numero_de_dias)
  #Se muestra un mensaje con el calculo de los promedio
    print(f"La temperatura promedio de la semana es: {promedio_semanal:.2f} °C")
  #en caso que no hayan datos se mostrara un mensaje diferente
else:
  print("No hay datos de temperatura para calcular el promedio.")
