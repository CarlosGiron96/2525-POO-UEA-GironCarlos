from producto import Producto

class Inventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        self.nombre_archivo = nombre_archivo
        self.productos = []
        self._cargar_inventario()

    def _cargar_inventario(self):
        try:
            with open(self.nombre_archivo, 'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
            print("Inventario cargado exitosamente.")
        except FileNotFoundError:
            print("Archivo 'inventario.txt' no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Error: No tiene permisos para leer el archivo 'inventario.txt'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al cargar el inventario: {e}")

    def _guardar_inventario(self):
        try:
            productos_ordenados = sorted(self.productos, key=lambda p: p.get_id_producto())
            with open(self.nombre_archivo, 'w') as file:
                for producto in productos_ordenados:
                    file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")
            print("Cambios guardados en el archivo.")
        except PermissionError:
            print("Error: No tiene permisos para escribir en el archivo 'inventario.txt'.")
        except Exception as e:
            print(f"Ocurrió un error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, producto):
        if any(p.get_id_producto() == producto.get_id_producto() for p in self.productos):
            print("Error: El ID del producto ya existe.")
            return
        self.productos.append(producto)
        self._guardar_inventario()
        self.ordenar_inventario_por_id()
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        producto_encontrado = None
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                producto_encontrado = producto
                break
        if producto_encontrado:
            self.productos.remove(producto_encontrado)
            self._guardar_inventario()
            self.ordenar_inventario_por_id()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        producto_encontrado = None
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                producto_encontrado = producto
                break
        if producto_encontrado:
            if nueva_cantidad is not None:
                producto_encontrado.set_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                producto_encontrado.set_precio(nuevo_precio)
            self._guardar_inventario()
            self.ordenar_inventario_por_id()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    def mostrar_todos_productos(self):
        try:
            with open(self.nombre_archivo, 'r') as file:
                print(" Inventario Actual ")
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    print(f"ID: {id_producto}, Nombre: {nombre}, Cantidad: {cantidad}, Precio: {precio}")
                print("-------------------------")
        except FileNotFoundError:
            print("El inventario está vacío o el archivo no se ha creado aún.")
        except Exception as e:
            print(f"Ocurrió un error al leer el archivo: {e}")

    def ordenar_inventario_por_id(self):
        self._guardar_inventario()
        print("El inventario ha sido ordenado y guardado.")