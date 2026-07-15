#examen transversal
peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
    }
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
    }

def cupos_por_género(titulo):
    cant = 0
    for género in peliculas:
        gen = peliculas[género][1]
        if gen.lower() == titulo.lower():
            cant += cartelera[género][-1]
    print("EL stock es:", cant)

def búsqueda_de_películas_por_rango_de_precio(p_min, p_max):
    l = []
    for género in cartelera:
        precio, cant = cartelera[género]
        if precio >= p_min and precio <= p_max:
            if cant != 0:
                nombre = peliculas[género][0]
                s = nombre + "--" + género
                l.append(s)
    if len(l) == 0:
        print("No hay películas en ese rango de precio.")
    else:
        print("Películas en el rango de precio:")
        for p in l:
            print(p)

def Actualizar_precio_de_película(codigo, nuevo_precio):
    if codigo in cartelera:
        precio, cant = cartelera[codigo]
        cartelera[codigo] = [nuevo_precio, cant]
        return True
    else:
        return False
def agregar_pelicula(p, titulo, género, duracion_min, clasificacion, idioma, es_3d, precio, cupos):
    if p not in peliculas:
        peliculas[p] = [titulo, género, duracion_min, clasificacion, idioma, es_3d]
        cartelera[p] = [precio, cupos]
        return True
    else:
        return False
def eliminar_pelicula(e):
    if e in peliculas:
        del peliculas[e]
        del cartelera[e]
        return True
    else:
        return False
def main():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Cupos por género.")
        print("2. Busqueda de películas por rango de precio.")
        print("3. Actualizar precio de la película.")
        print("4. Agregar película.")
        print("5. Eliminar película.")
        print("6. Salir.")
        op = input("Ingrese opción: ")
        if op == "6":
            print("Programa finalizado.")
            break
        elif op == "1":
            género = input("Ingrese género a consultar: ")
            cupos_por_género(género)
        elif op == "2":
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            búsqueda_de_películas_por_rango_de_precio(p_min, p_max)
        elif op == "3":
            codigo = input("Ingrese código de la película: ")
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if Actualizar_precio_de_película(codigo, nuevo_precio):
                print("Precio actualizado correctamente.")
            else:
                print("Código no encontrado.")
        elif op == "4":
            p = input("Ingrese código de la película: ")
            nombre = input("Ingrese nombre de la película: ")
            género = input("Ingrese género de la película: ")
            duracion = input("Ingrese duración de la película: ")
            clasificacion = input("Ingrese clasificación de la película: ")
            idioma = input("Ingrese idioma de la película: ")
            es_3d = input("¿Es 3D? (s/n): ").lower() == "s"
            precio = int(input("Ingrese precio de la película: "))
            cupos = int(input("Ingrese cupos de la película: "))
            if agregar_pelicula(p, nombre, género, duracion, clasificacion, idioma, es_3d, precio, cupos):
                print("Película agregada correctamente.")
            else:
                print("Código ya existe.")
        elif op == "5":
            p = input("Ingrese código de la película a eliminar: ")
            if eliminar_pelicula(p):
                print("Película eliminada correctamente.")
            else:
                print("Código no encontrado.")
        elif op == "6":
            print("programa finalizado. que tenga buen dia.")
            break
        else:
            print("Debe ingresar una opción válida!!")


if __name__ == "__main__":
    main()

        