"""Esta clase reperesetna a los libros ingresados en la biblioteca"""
from typing import Tuple
class Libro:
    """teniendo como atributos el titulo, autor, categoria e isbn"""
    def __init__(self, titulo: str, autor: str, categoria: str, isbn: str):
        # Usamos una tupla para almacenar el título y el autor, ya que son inmutables.
        self.info: Tuple[str, str] = (titulo, autor)
        self.categoria: str = categoria
        self.isbn: str = isbn
        self.disponible: bool = True

    def __repr__(self) -> str:
        """Esto es lo que se mostrara al llamar esta clase"""
        return f"Libro(Título: '{self.info[0]}', Autor: '{self.info[1]}', Categoría: '{self.categoria}', ISBN: '{self.isbn}')"

