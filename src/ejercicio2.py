#Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, finalizando cuando se introduzca “x”. 
#A continuación, solicitar que introduzca los nombres de los alumnos de secundaria, finalizando al introducir “x”.

#Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
#Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
#Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
#Mostrar si todos los nombres de primaria están incluidos en secundaria.

def obtener_nombres_alumnos():
    """
    Solicita al usuario que introduzca los nombres de los alumnos de primaria y secundaria.
    Finaliza la entrada cuando se introduce 'x'.

    Retorna:
    - set: Conjunto de nombres de los alumnos de primaria.
    - set: Conjunto de nombres de los alumnos de secundaria.
    """
    nombres_primaria = set()
    nombres_secundaria = set()

    print("Introduce los nombres de los alumnos de primaria (introduce 'x' para finalizar):")
    nombre_primaria = input()
    while nombre_primaria.lower() != 'x':
        nombres_primaria.add(nombre_primaria)
        nombre_primaria = input()

    print("Introduce los nombres de los alumnos de secundaria (introduce 'x' para finalizar):")
    nombre_secundaria = input()
    while nombre_secundaria.lower() != 'x':
        nombres_secundaria.add(nombre_secundaria)
        nombre_secundaria = input()

    return nombres_primaria, nombres_secundaria

def mostrar_resultados(nombres_primaria, nombres_secundaria):
    """
    Muestra los resultados de operaciones con conjuntos de nombres de alumnos.

    Parámetros:
    - nombres_primaria (set): Conjunto de nombres de los alumnos de primaria.
    - nombres_secundaria (set): Conjunto de nombres de los alumnos de secundaria.
    """
    print("\nNombres de todos los alumnos de primaria y secundaria sin repeticiones:")
    nombres_totales = nombres_primaria.union(nombres_secundaria)
    print(nombres_totales)

    print("\nNombres que se repiten entre primaria y secundaria:")
    nombres_repetidos = nombres_primaria.intersection(nombres_secundaria)
    print(nombres_repetidos)

    print("\nNombres de primaria que no se repiten en secundaria:")
    nombres_no_repetidos_secundaria = nombres_primaria.difference(nombres_secundaria)
    print(nombres_no_repetidos_secundaria)

    print("\n¿Todos los nombres de primaria están incluidos en secundaria?")
    todos_incluidos = nombres_primaria.issubset(nombres_secundaria)
    print(todos_incluidos)

if __name__ == "__main__":
    nombres_primaria, nombres_secundaria = obtener_nombres_alumnos()
    mostrar_resultados(nombres_primaria, nombres_secundaria)
