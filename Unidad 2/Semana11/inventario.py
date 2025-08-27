from producto import Producto
import os

class Inventario:
    """
    Gestiona un inventario de productos utilizando un diccionario.
    Las claves son los IDs de los productos y los valores son objetos de la clase Producto.
    """

    def __init__(self, nombre_archivo="inventario.txt"):
        self.nombre_archivo = nombre_archivo
        self.productos = {}  # Ahora es un diccionario
        self._cargar_inventario()

    def _cargar_inventario(self):
        try:
            if not os.path.exists(self.nombre_archivo):
                print("Archivo 'inventario.txt' no encontrado. Se creará uno nuevo al guardar.")
                return

            with open(self.nombre_archivo, 'r') as file:
                for line in file:
                    try:
                        id_producto, nombre, cantidad_str, precio_str = line.strip().split(',')
                        producto = Producto(id_producto, nombre, int(cantidad_str), float(precio_str))
                        self.productos[id_producto] = producto
                    except (ValueError, IndexError) as e:
                        print(
                            f"Advertencia: Línea con formato incorrecto en el archivo '{self.nombre_archivo}': '{line.strip()}'. Error: {e}")
            print("Inventario cargado exitosamente.")
        except PermissionError:
            print("Error: No tiene permisos para leer el archivo 'inventario.txt'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al cargar el inventario: {e}")

    def _guardar_inventario(self):
        try:
            productos_ordenados = sorted(self.productos.values(), key=lambda p: p.get_id_producto())
            with open(self.nombre_archivo, 'w') as file:
                for producto in productos_ordenados:
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Cambios guardados en el archivo.")
        except PermissionError:
            print("Error: No tiene permisos para escribir en el archivo 'inventario.txt'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: El ID del producto ya existe.")
            return
        self.productos[producto.get_id_producto()] = producto
        self._guardar_inventario()
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self._guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            producto_encontrado = self.productos[id_producto]
            if nueva_cantidad is not None:
                producto_encontrado.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto_encontrado.set_precio(nuevo_precio)
            self._guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        nombre_lower = nombre.lower()
        for producto in self.productos.values():
            if nombre_lower in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- Inventario Actual ---")
        # Iteramos sobre los elementos ordenados por ID para una salida consistente
        for id_producto in sorted(self.productos.keys()):
            print(self.productos[id_producto])
        print("-------------------------")