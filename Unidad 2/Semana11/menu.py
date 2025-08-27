from inventario import Inventario
from producto import Producto


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
                if id_producto in inventario.productos:
                    print("Error: El ID del producto ya existe.")
                    continue
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
                print("\nResultados de la búsqueda:")
                for producto in resultados:
                    print(producto)
            else:
                print("No se encontraron productos que coincidan con la búsqueda.")

        elif opcion == '5':
            inventario.mostrar_todos_productos()

        elif opcion == '6':
            print("Saliendo")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
