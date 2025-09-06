"""Gestiona la colección de libros y usuarios de la biblioteca, así como los libros préstamos."""
import os
from libro import Libro
from usuario import Usuario
from typing import Set, List, Dict

class Biblioteca:

    def __init__(self):
        self.libros: Dict[str, Libro] = {}
        self.usuarios_ids: Set[str] = set()
        self.usuarios: Dict[str, Usuario] = {}
        # Cargar datos al inicializar la biblioteca
        self.cargar_datos()

    def agregar_libro(self, libro: Libro) -> str:
        """Añade un libro a la biblioteca si su ISBN no existe."""
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            return f"Libro '{libro.info[0]}' agregado exitosamente."
        return "Error: El libro con este ISBN ya existe."

    def quitar_libro(self, isbn: str) -> str:
        """Quita un libro de la biblioteca por su ISBN."""
        if isbn in self.libros:
            del self.libros[isbn]
            return f"Libro con ISBN '{isbn}' eliminado exitosamente."
        return "Error: El libro no se encontró."

    def registrar_usuario(self, usuario: Usuario) -> str:
        """Registra un nuevo usuario si su ID es único."""
        if usuario.user_id not in self.usuarios_ids:
            self.usuarios_ids.add(usuario.user_id)
            self.usuarios[usuario.user_id] = usuario
            return f"Usuario '{usuario.nombre}' registrado exitosamente."
        return "Error: El ID de usuario ya está en uso."

    def dar_de_baja_usuario(self, user_id: str) -> str:
        """Da de baja a un usuario si existe y no tiene libros prestados."""
        if user_id in self.usuarios_ids:
            usuario = self.usuarios[user_id]
            if not usuario.libros_prestados:
                self.usuarios_ids.remove(user_id)
                del self.usuarios[user_id]
                return f"Usuario con ID '{user_id}' dado de baja exitosamente."
            return "Error: El usuario tiene libros prestados y no puede ser dado de baja."
        return "Error: El usuario no se encontró."

    def prestar_libro(self, user_id: str, isbn: str) -> str:
        """Presta un libro a un usuario si el libro está disponible."""
        if user_id not in self.usuarios:
            return "Error: Usuario no encontrado."
        if isbn not in self.libros:
            return "Error: Libro no encontrado."

        libro = self.libros[isbn]
        usuario = self.usuarios[user_id]

        if libro.disponible:
            libro.disponible = False
            usuario.libros_prestados.append(libro)
            return f"Libro '{libro.info[0]}' prestado a '{usuario.nombre}'."
        return "Error: El libro no está disponible para préstamo."

    def devolver_libro(self, user_id: str, isbn: str) -> str:
        """Permite a un usuario devolver un libro."""
        if user_id not in self.usuarios:
            return "Error: Usuario no encontrado."
        if isbn not in self.libros:
            return "Error: Libro no encontrado."

        libro = self.libros[isbn]
        usuario = self.usuarios[user_id]

        if libro in usuario.libros_prestados:
            libro.disponible = True
            usuario.libros_prestados.remove(libro)
            return f"Libro '{libro.info[0]}' devuelto por '{usuario.nombre}'."
        return "Error: El libro no fue prestado a este usuario."

    def buscar_libro(self, consulta: str, tipo: str = 'titulo') -> List[Libro]:
        """Busca libros por título, autor o categoría."""
        resultados: List[Libro] = []
        for libro in self.libros.values():
            if tipo == 'titulo' and consulta.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif tipo == 'autor' and consulta.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif tipo == 'categoria' and consulta.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, user_id: str) -> List[Libro]:
        """Lista los libros prestados a un usuario específico."""
        if user_id in self.usuarios:
            return self.usuarios[user_id].libros_prestados
        return []

    def listar_libros(self) -> None:
        """Muestra una lista de todos los libros en la biblioteca."""
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("\n--- Catálogo de Libros ---")
            for isbn, libro in self.libros.items():
                estado = "Disponible" if libro.disponible else "Prestado"
                print(f"ISBN: {isbn} | Título: {libro.info[0]} | Autor: {libro.info[1]} | Estado: {estado}")
            print("------------------------")

    def listar_usuarios(self) -> None:
        """Muestra una lista de todos los usuarios registrados."""
        if not self.usuarios:
            print("No hay usuarios registrados.")
        else:
            print("\n--- Lista de Usuarios ---")
            for user_id, usuario in self.usuarios.items():
                print(f"ID: {user_id} | Nombre: {usuario.nombre}")
            print("-------------------------")

    def guardar_datos(self):
        """Guarda todos los datos de la biblioteca en archivos de texto."""
        try:
            with open("libros.txt", "w") as f_libros:
                for libro in self.libros.values():
                    # Formato: titulo|autor|categoria|isbn|disponible
                    f_libros.write(
                        f"{libro.info[0]}|{libro.info[1]}|{libro.categoria}|{libro.isbn}|{libro.disponible}\n")

            with open("usuarios.txt", "w") as f_usuarios:
                for usuario in self.usuarios.values():
                    # Formato: nombre|user_id|isbn1,isbn2,...
                    libros_prestados_isbns = ",".join([libro.isbn for libro in usuario.libros_prestados])
                    f_usuarios.write(f"{usuario.nombre}|{usuario.user_id}|{libros_prestados_isbns}\n")
            print("\nDatos guardados exitosamente.")
        except IOError as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_datos(self):
        """Carga los datos de los archivos de texto al iniciar el programa."""
        try:
            # Cargar libros
            with open("libros.txt", "r") as f_libros:
                for linea in f_libros:
                    titulo, autor, categoria, isbn, disponible_str = linea.strip().split('|')
                    libro = Libro(titulo, autor, categoria, isbn)
                    libro.disponible = (disponible_str == 'True')
                    self.libros[isbn] = libro

            # Cargar usuarios
            with open("usuarios.txt", "r") as f_usuarios:
                for linea in f_usuarios:
                    partes = linea.strip().split('|')
                    nombre, user_id = partes[0], partes[1]
                    usuario = Usuario(nombre, user_id)
                    self.usuarios[user_id] = usuario
                    self.usuarios_ids.add(user_id)

                    if len(partes) > 2 and partes[2]:
                        isbns_prestados = partes[2].split(',')
                        for isbn in isbns_prestados:
                            if isbn in self.libros:
                                usuario.libros_prestados.append(self.libros[isbn])

            print("\nDatos cargados exitosamente.")
        except FileNotFoundError:
            print("\nArchivos de datos no encontrados. Se iniciará con una biblioteca vacía.")
        except Exception as e:
            print(f"Ocurrió un error al cargar los datos: {e}")

