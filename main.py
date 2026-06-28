from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear el restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto("Hamburguesa", 5.50, 10, True)
producto2 = Producto("Pizza", 8.00, 5, True)

# Crear clientes
cliente1 = Cliente("Ana Pérez", 20, "ana@gmail.com", True)
cliente2 = Cliente("Luis Gómez", 30, "luis@gmail.com", False)

# Agregar productos al restaurante
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()