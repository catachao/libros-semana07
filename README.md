# Funcionamiento del código de Biblioteca

El siguiente código Python define dos clases: `Libro` y `Biblioteca`, junto con algunas excepciones personalizadas y una función principal `main`.

## Función `main()`

La función `main()` permite al usuario interactuar con la biblioteca a través de un menú interactivo que incluye las siguientes opciones:

1. Agregar libros
2. Buscar libros por título
3. Mostrar todos los libros en la biblioteca
4. Salir del programa.

## Clase Libro

La clase `Libro` tiene los siguientes atributos:

- `titulo`: El título del libro.
- `autor`: El autor del libro.
- `año_publicacion`: El año de publicación del libro.

## Clase Biblioteca

La clase `Biblioteca` administra una lista de libros. Tiene los siguientes métodos:

- `agregar_libro(libro)`: Agrega un libro a la biblioteca.
- `buscar_libro(titulo)`: Busca un libro por título.
- `mostrar_libros()`: Muestra todos los libros en la biblioteca.

## Excepciones Personalizadas

El código define dos excepciones personalizadas: `ErrorLibroSinTitulo` y `ErrorLibroSinAutor`, que se lanzan cuando se intenta agregar un libro sin título o sin autor, respectivamente.
