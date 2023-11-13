#Dado el conjunto de números enteros:

#numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Crea un conjunto pares que contenga los números pares del conjunto numeros.
#Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
#Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.

def operaciones_con_conjuntos(numeros):
    """
    Realiza operaciones con conjuntos a partir de un conjunto dado de números.

    Parámetros:
    - numeros (set): Conjunto de números enteros.

    Retorna:
    - set: Conjunto de números pares.
    - set: Conjunto de números múltiplos de tres.
    - set: Intersección entre los conjuntos de pares y múltiplos de tres.
    """
    pares = set(num for num in numeros if num % 2 == 0)
    multiplos_de_tres = set(num for num in numeros if num % 3 == 0)
    pares_y_multiplos_de_tres = pares.intersection(multiplos_de_tres)

    return pares, multiplos_de_tres, pares_y_multiplos_de_tres

if __name__ == "__main__":
    numeros = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    resultados = operaciones_con_conjuntos(numeros)

    print("Conjunto de números pares:", resultados[0])
    print("Conjunto de múltiplos de tres:", resultados[1])
    print("Intersección entre pares y múltiplos de tres:", resultados[2])
