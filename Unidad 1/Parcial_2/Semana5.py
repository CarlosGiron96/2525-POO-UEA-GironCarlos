#Transformar de grados celcius a fahrenheit
def convertir_celsius_a_fahrenheit(grados_celsius):
    grados_fahrenheit = (grados_celsius * 9/5) + 32
    return grados_fahrenheit

#Transformar de metros a pies
def convertir_metros_a_pies(metros):
    pies = metros * 3.28084
    return pies
#Lineas para calcular el descuento de un producto
def calcular_descuento(precio_original, porcentaje_descuento):
    if not isinstance(precio_original, (int, float)) or precio_original < 0:
        raise ValueError("El precio original debe ser un número positivo.")
    if not isinstance(porcentaje_descuento, (int, float)) or porcentaje_descuento < 0 or porcentaje_descuento > 100:
        raise ValueError("El porcentaje de descuento debe ser un número entre 0 y 100.")
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final
#Para facilitar la navegacion se incluye un menu de opciones
def mostrar_menu():
    print("Seleccione una opción de conversión:")
    print("1. Grados Celsius a Fahrenheit")
    print("2. Metros a pies")
    print("3. Salir")
#se ejecuta utilizando todos los ejemplos
if __name__ == "__main__":
    try:
        precio_producto = 100.0
        porcentaje = 20
        precio_con_descuento = calcular_descuento(precio_producto, porcentaje)
        print(f"Precio original: ${precio_producto:.2f}")
        print(f"Descuento: {porcentaje}%")
        print(f"Precio con descuento: ${precio_con_descuento:.2f}")

#En caso que se ingrese un valor negativo
        precio_invalido = -50.0
        porcentaje_invalido = -10

    except ValueError as e:
        print(f"Error: {e}")
        #para utilizar el menu se ejecuta:
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de opción: ")

        if opcion == '1':
            grados_celsius = float(input("Ingrese la cantidad de grados Celsius: "))
            grados_fahrenheit = convertir_celsius_a_fahrenheit(grados_celsius)
            print(f"{grados_celsius} grados Celsius son {grados_fahrenheit:.2f} grados Fahrenheit\n")
        elif opcion == '2':
            metros = float(input("Ingrese la cantidad de metros: "))
            pies = convertir_metros_a_pies(metros)
            print(f"{metros} metros son {pies:.2f} pies\n")
        elif opcion == '3':
            print("Gracias")
            break
        else:
            print("Por favor, seleccione una opción válida.\n")
