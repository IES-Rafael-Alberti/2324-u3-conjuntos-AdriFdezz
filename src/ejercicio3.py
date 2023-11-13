#El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

#Por ejemplo, el conjunto potencia de {1,2,3} es:

#{∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}
#Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y retorne su «lista potencia» (la lista de todos sus subconjuntos):

#>>> conjunto_potencia({6, 1, 4})
#[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]

def conjunto_potencia(s):
    """
    Retorna la lista de todos los subconjuntos del conjunto dado.

    Parámetros:
    - s (set): Conjunto de entrada.

    Retorna:
    - list: Lista de subconjuntos de s.
    """
    elementos = list(s)
    lista_potencia = [set()]

    for elemento in elementos:
        lista_potencia.extend([subset.union({elemento}) for subset in lista_potencia])

    return lista_potencia

if __name__ == "__main__":
    conjunto_entrada = {6, 1, 4}
    resultado = conjunto_potencia(conjunto_entrada)
    print(resultado)