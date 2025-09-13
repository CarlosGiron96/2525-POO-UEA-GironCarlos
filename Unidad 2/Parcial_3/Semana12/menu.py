import os
from libro import Libro
from usuario import Usuario
from biblioteca import Biblioteca


def mostrar_menu():
    """Muestra el menú de opciones en la consola."""
    print("\n--- Menú de la Biblioteca ---")
    print("1. Agregar un libro")
    print("2. Eliminar un libro")
    print("3. Registrar un usuario")
    print("4. Suprimir un usuario")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Buscar libros")
    print("8. Listar libros prestados de un usuario")
    print("9. Lista de todos los libros")
    print("10. Lista de todos los usuarios")
    print("0. Salir y Guardar")
    print("------------------------------")


def main():

    biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Ingrese el título del libro: ")
            autor = input("Ingrese el autor del libro: ")
            categoria = input("Ingrese la categoría del libro: ")
            isbn = input("Ingrese el ISBN del libro: ")
            libro = Libro(titulo, autor, categoria, isbn)
            print(biblioteca.agregar_libro(libro))

        elif opcion == "2":
            isbn = input("Ingrese el ISBN del libro a quitar: ")
            print(biblioteca.quitar_libro(isbn))

        elif opcion == "3":
            nombre = input("Ingrese el nombre del usuario: ")
            user_id = input("Ingrese el ID del usuario: ")
            usuario = Usuario(nombre, user_id)
            print(biblioteca.registrar_usuario(usuario))

        elif opcion == "4":
            user_id = input("Ingrese el ID del usuario a dar de baja: ")
            print(biblioteca.dar_de_baja_usuario(user_id))

        elif opcion == "5":
            user_id = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a prestar: ")
            print(biblioteca.prestar_libro(user_id, isbn))

        elif opcion == "6":
            user_id = input("Ingrese el ID del usuario: ")
            isbn = input("Ingrese el ISBN del libro a devolver: ")
            print(biblioteca.devolver_libro(user_id, isbn))

        elif opcion == "7":
            criterio = input("Buscar por (titulo/autor/categoria): ").lower()
            consulta = input(f"Ingrese la consulta de búsqueda por {criterio}: ")
            resultados = biblioteca.buscar_libro(consulta, criterio)
            if resultados:
                print("\n--- Resultados de Búsqueda ---")
                for libro in resultados:
                    print(f"  - Título: {libro.info[0]}, Autor: {libro.info[1]}, ISBN: {libro.isbn}")
                print("------------------------------")
            else:
                print("No se encontraron resultados.")

        elif opcion == "8":
            user_id = input("Ingrese el ID del usuario: ")
            libros_prestados = biblioteca.listar_libros_prestados(user_id)
            if libros_prestados:
                print(f"\n--- Libros prestados a '{user_id}' ---")
                for libro in libros_prestados:
                    print(f"  - Título: {libro.info[0]}, Autor: {libro.info[1]}")
                print("-----------------------------------")
            else:
                print("No se encontraron libros prestados o el usuario no existe.")

        elif opcion == "9":
            biblioteca.listar_libros()

        elif opcion == "10":
            biblioteca.listar_usuarios()

        elif opcion == "0":
            biblioteca.guardar_datos()
            print("Saliendo del sistema. ¡Hasta pronto!")
            break

        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()
