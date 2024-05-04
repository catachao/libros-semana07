class Libro:
    def __init__(self, titulo, autor, año_publicacion):
        if not titulo:
            raise ErrorLibroSinTitulo
        if not autor:
            raise ErrorLibroSinAutor

        while True:
            try:
                self.año_publicacion = int(año_publicacion)
                if self.año_publicacion < 0:
                    raise ValueError("El año de publicación no puede ser negativo.")
                break  # Salir del bucle si el año es válido
            except ValueError:
                print("Error: El año de publicación debe ser un número entero.")
                año_publicacion = input("Ingrese el año de publicación nuevamente: ")

        self.titulo = titulo
        self.autor = autor



class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado a la biblioteca.")

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        raise ValueError(f"No se encontró ningún libro con el título '{titulo.lower()}'.")

    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                print(f"- {libro.titulo} (Autor: {libro.autor}, Año: {libro.año_publicacion})")


class ErrorLibroSinTitulo(Exception):
    def __init__(self, mensaje="El libro debe tener un título."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorLibroSinAutor(Exception):
    def __init__(self, mensaje="El libro debe tener un autor."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


def main():
    biblioteca = Biblioteca()

    while True:
        print("\nMenú:")
        print("1. Agregar libro")
        print("2. Buscar libro por título")
        print("3. Mostrar todos los libros")
        print("4. Salir del programa")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                titulo = input("Ingrese el título del libro: ")
                autor = input("Ingrese el autor del libro: ")
                año_publicacion = input("Ingrese el año de publicación del libro: ")

                libro = Libro(titulo, autor, año_publicacion)
                biblioteca.agregar_libro(libro)
            except (ErrorLibroSinTitulo, ErrorLibroSinAutor) as e:
                print(e)

        elif opcion == "2":
            titulo = input("Ingrese el título del libro a buscar: ")
            try:
                libro_encontrado = biblioteca.buscar_libro(titulo.lower())  # Convertir a minúsculas
                print(f"Libro encontrado: {libro_encontrado.titulo} (Autor: {libro_encontrado.autor}, Año: {libro_encontrado.año_publicacion})")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            biblioteca.mostrar_libros()

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()