# Clase que representa un cliente del restaurante

class Cliente:

    def __init__(self, nombre: str, edad: int, correo: str, es_frecuente: bool):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
        self.es_frecuente = es_frecuente

    def __str__(self):
        return f"{self.nombre} | Edad: {self.edad} | Correo: {self.correo} | Frecuente: {self.es_frecuente}"