from modelos.producto import Producto
from modelos.cliente import Cliente

# Clase que gestiona productos y clientes del restaurante
class Restaurante:

    def __init__(self):
        # Listas para almacenar objetos
        self.productos = []
        self.clientes = []

    # Agregar producto a la lista
    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    # Agregar cliente a la lista
    def agregar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)

    # Mostrar productos
    def mostrar_productos(self):
        print("\n--- PRODUCTOS ---")
        for producto in self.productos:
            print(producto)

    # Mostrar clientes
    def mostrar_clientes(self):
        print("\n--- CLIENTES ---")
        for cliente in self.clientes:
            print(cliente)