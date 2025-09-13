"""Esta Clase es la representacion de un usuario ingresado en la biblioteca"""
from typing import  List
from libro import Libro

class Usuario:
    """teniendo como puntos el nombre, id, lista de libros prestados"""
    def __init__(self, nombre: str, user_id: str):
        self.nombre: str = nombre
        self.user_id: str = user_id
        # Lista para gestionar los libros que el usuario tiene prestados.
        self.libros_prestados: List[Libro] = []

    def __repr__(self) -> str:
        """esto lo que se retorna al llamar a esta clase"""
        return f"Usuario(Nombre: '{self.nombre}', ID: '{self.user_id}', Libros prestados: {len(self.libros_prestados)})"
