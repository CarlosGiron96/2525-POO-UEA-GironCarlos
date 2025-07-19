#primero se crea una clase donde se llame a los productos de la tienda
class Producto:
    def __init__(self, nombre, precio, cant_stock):
        self.nombre = nombre
        self.precio = precio
        self.cant_stock = cant_stock
    #En caso de aquirir mas productos con el comando se puede agregar mas
    def actualizar_cantidad(self, cantidad):
        self.cant_stock += cantidad

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio:.2f} - Disponible: {self.cant_stock}"

#Emulando una factura se detalla las ventas realizadas con una lista donde se muestra
#nombre de prodcuto, la cantidad comprada, la fecha que se realiza la compra y el precio total.
class Venta:
    def __init__(self, producto, cantidad, fecha):
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.total = self.calcular_total()
    #Operacion para calcular el precio total segun la cantidad y el precio del producto
    def calcular_total(self):
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"Venta de {self.cantidad} {self.producto.nombre} el {self.fecha} - Total: ${self.total:.2f}"


class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = {}
        self.ventas = []

    def agregar_producto(self, producto):
        self.productos[producto.nombre] = producto

    def realizar_venta(self, nombre_producto, cantidad, fecha):
        if nombre_producto in self.productos:
            producto = self.productos[nombre_producto]
            if producto.cant_stock >= cantidad:
                venta = Venta(producto, cantidad, fecha)
                self.ventas.append(venta)
                producto.actualizar_cantidad(-cantidad)
                print(f"Venta exitosa de {cantidad} {nombre_producto}")
            else:
                print(f"No hay suficiente stock de {nombre_producto}")
        else:
            print(f"Producto {nombre_producto} no encontrado")

    def mostrar_inventario(self):
        print(f"\nInventario de {self.nombre}:")
        for nombre, producto in self.productos.items():
            print(producto)

    def mostrar_ventas(self):
        print(f"\nHistorial de ventas de {self.nombre}:")
        for venta in self.ventas:
            print(venta)

#pequeño ejemplo de como se puede usar el codigo
if __name__ == "__main__":
    tienda = Tienda("El Esquimal Perdido")

    #Primero agregamos productos
    producto1 = Producto("Bloque de hielo", 2.5, 30)
    producto2 = Producto("Lapiz sin punta", 0.4, 200)
    tienda.agregar_producto(producto1)
    tienda.agregar_producto(producto2)

    #Antes de vender se verifica el inventario
    tienda.mostrar_inventario()

    #LAs ventas se hace con el nombre del prodcuto, la cantidad y la fecha
    tienda.realizar_venta("Bloque de hielo", 2, "2024-06-19")
    tienda.realizar_venta("Lapiz sin punta", 5, "2024-06-19")
    tienda.realizar_venta("Bloque de hielo", 10, "2024-06-19")  # Stock insuficiente

    #una vez realizado las ventas se muestra de nuevo el inventario ya con los productos vendidos menos
    tienda.mostrar_inventario()

    #Como extra se muestra todas las ventas del dia
    tienda.mostrar_ventas()