#primero se crea una clase donde se guarde el nombre del producto junto al precio del mismo
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
#Se crea una clase donde se guarden los datos de una factura, este contendra
#nombre del cliente, el numero de la factura y los productos adquiridos
class Factura:
    def __init__(self, cliente, num_factura):
        self.cliente = cliente
        self.num_factura = num_factura
        self.productos = []
    #A continucion se agragan productos a la factura
    def agregar_producto(self, producto):
        self.productos.append(producto)
    #Se suma los valores guardados en precio de cada uno de los productos enlistados
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total
    #Se imprime en orden el numero de la factura, el cliente , los productos y la sumatoria total
    def __str__(self):
        factura_str = f"Factura # {self.num_factura} para {self.cliente}\n"
        for producto in self.productos:
            factura_str += str(producto) + "\n"
        factura_str += f"Total: ${self.calcular_total()}\n"
        return factura_str
#En la factura de venta se genera un descuento segun el producto
class FacturaVenta(Factura):
    def __init__(self, cliente, num_factura, descuento):
        super().__init__(cliente, num_factura)
        self.descuento = descuento
    #se calcula el valor sin tomar en cuenta el descuento
    def calcular_total(self):
        total_sin_descuento = super().calcular_total()
        return total_sin_descuento * (1 - self.descuento)
    #Se resta el descuento del valor final
    def calcular_descuento(self):
        total_sin_descuento = super().calcular_total()
        desc = total_sin_descuento * self.descuento
        return total_sin_descuento - desc
    #Se imprime en pantalla la fctura
    def __str__(self):
        return f"Factura Venta {super().__str__()}\nDescuento: {self.descuento * 100}%\nTotal con descuento: ${self.calcular_descuento()}"
#Al diferencia de la factura de venta, en esta se añade un porcentaje de iva
class FacturaServicio(Factura):
    def __init__(self, cliente, num_factura, iva):
        super().__init__(cliente, num_factura)
        self.iva = iva
    #Se calcula el iva y se lo ruma a la suma de los valores de los productos
    def calcular_total(self):
        total_sin_iva = super().calcular_total()
        return total_sin_iva + (total_sin_iva * self.iva)

    def __str__(self):
        return f"\nFactura Servicio {super().__str__()}\nIva: {self.iva * 100}%\nTotal con iva: ${self.calcular_total()}\n"

# Ejemplo
producto1 = Producto("Cpu", 250)
producto2 = Producto("Pantalla", 150)
factura1 = Factura("Marcos Velasquez", "0045")
factura1.agregar_producto(producto1)
factura1.agregar_producto(producto2)
print(factura1)

factura_venta = FacturaVenta("Vidal Hidalgo", "0049", 0.15)
factura_venta.agregar_producto(Producto("Ps5", 680))
print(factura_venta)

factura_servicio = FacturaServicio("Carlos Giron", "0125", 0.22)
factura_servicio.agregar_producto(Producto("Reparacion", 230))
print(factura_servicio)