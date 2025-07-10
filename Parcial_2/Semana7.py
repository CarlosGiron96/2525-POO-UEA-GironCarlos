import time

class Archivo:
    #Se abre el archivo para ingresar datos
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, 'w')
        print(f"Archivo '{self.nombre_archivo}' abierto para escritura.")
    #Se cierra el archivo despues de escribir los datos
    def __del__(self):
        if self.archivo:
            self.archivo.close()
            print(f"Archivo '{self.nombre_archivo}' cerrado.")

#Simulador de conectar a un servidor local
class Conexion:
    #Con el siguiente inicializador se hara una conexion a un servidor local
    def __init__(self, servidor, puerto):
        self.servidor = servidor
        self.puerto = puerto
        print(f"Conexión establecida con {self.servidor}:{self.puerto}")
        time.sleep(1)

#Con el siguiente destructor se cierra la conexion a un servidor
    def __del__(self):
        print(f"Cerrando conexión con {self.servidor}:{self.puerto}")
        time.sleep(1)

def mostrar_lista(leer):
    if leer == "si" or leer == "SI" or leer == "sI" or leer == "Si":
        try:
            with open("Datos_Personales.txt", "r") as archivo:
                #Leer el contenido del archivo
                contenido = archivo.read()

                #Imprimir el contenido (o procesarlo)
                print(contenido)

        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    return("Se cerro el programa")

#utilizar los codigos anteriores
if __name__ == "__main__":
    # Escribir algo en el archivo
    conexion = Conexion("localhost", 8080)
    nombre = input("Por favor, ingresa tu nombre: ")
    apellido = input("Por favor, ingresa tu apellido: ")
    edad = input("Por favor, ingresa tu edad: ")
    profesion = input("Por favor, ingresa tu profesion: ")
    observaciones = input("Por favor, ingresa tu observaciones: ")
    datos_persona = [nombre, apellido, edad, profesion, observaciones]
    with open("Datos_Personales.txt", "w") as archivo:
        archivo.writelines([elemento + "\n" for elemento in datos_persona])

    del archivo
    del conexion
    print("Se ha escrito el archivo de texto")

    mostrar_lista(leer = input("Quiere leer el archivo de texto: "))

