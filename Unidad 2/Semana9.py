class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"


class Inventario:
     def __init__(self):
        self.productos = []

     def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        print("Producto añadido exitosamente.")

     def eliminar_producto(self, id_producto):
        producto_encontrado = None
        for producto in self.productos:
            if producto.get_id_producto() == id_producto:
                producto_encontrado = producto
                break
        if producto_encontrado:
            self.productos.remove(producto_encontrado)
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
         if not self.productos:
            print("El inventario está vacío.")
         else:
            print("--- Inventario Actual ---")
            for producto in self.productos:
                print(producto)
            print("-------------------------")

def main():
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir nuevo producto")
        print("2. Eliminar producto por ID")
        print("3. Actualizar producto por ID")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                id_producto = input("Ingrese el ID del producto: ")
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad: "))
                precio = float(input("Ingrese el precio: "))
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Entrada inválida. La cantidad debe ser un número entero y el precio un número.")

        elif opcion == '2':
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == '3':
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("¿Qué desea actualizar?")
            print("1. Cantidad")
            print("2. Precio")
            print("3. Ambos")
            opc_act = input("Seleccione una opción: ")

            nueva_cantidad = None
            nuevo_precio = None

            if opc_act == '1' or opc_act == '3':
                try:
                    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
                except ValueError:
                    print("Entrada inválida. La cantidad debe ser un número entero.")
                    continue

            if opc_act == '2' or opc_act == '3':
                try:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                except ValueError:
                    print("Entrada inválida. El precio debe ser un número.")
                    continue

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == '4':
            nombre = input("Ingrese el nombre (o parte) del producto a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            if resultados:
                print("\n--- Resultados de la búsqueda ---")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos que coincidan con la búsqueda.")

        elif opcion == '5':
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()