#Dadas las siguientes listas:

#frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
#frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
#Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
#Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
#Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
#Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

def obtener_conjuntos(frutas1, frutas2):
    """
    Crea conjuntos a partir de las listas de frutas.

    Parámetros:
    - frutas1 (list): Lista de frutas 1.
    - frutas2 (list): Lista de frutas 2.

    Retorna:
    - set: Conjunto de frutas 1.
    - set: Conjunto de frutas 2.
    """
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    return set_frutas1, set_frutas2

def encontrar_frutas_comunes(set_frutas1, set_frutas2):
    """
    Encuentra las frutas comunes entre dos conjuntos.

    Parámetros:
    - set_frutas1 (set): Conjunto de frutas 1.
    - set_frutas2 (set): Conjunto de frutas 2.

    Retorna:
    - set: Conjunto de frutas comunes.
    """
    return set_frutas1.intersection(set_frutas2)

def encontrar_frutas_solo_en_frutas1(set_frutas1, set_frutas2):
    """
    Encuentra las frutas que están en frutas1 pero no en frutas2.

    Parámetros:
    - set_frutas1 (set): Conjunto de frutas 1.
    - set_frutas2 (set): Conjunto de frutas 2.

    Retorna:
    - set: Conjunto de frutas solo en frutas1.
    """
    return set_frutas1.difference(set_frutas2)

def encontrar_frutas_solo_en_frutas2(set_frutas1, set_frutas2):
    """
    Encuentra las frutas que están en frutas2 pero no en frutas1.

    Parámetros:
    - set_frutas1 (set): Conjunto de frutas 1.
    - set_frutas2 (set): Conjunto de frutas 2.

    Retorna:
    - set: Conjunto de frutas solo en frutas2.
    """
    return set_frutas2.difference(set_frutas1)

if __name__ == "__main__":
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1, set_frutas2 = obtener_conjuntos(frutas1, frutas2)

    frutas_comunes = encontrar_frutas_comunes(set_frutas1, set_frutas2)
    frutas_solo_en_frutas1 = encontrar_frutas_solo_en_frutas1(set_frutas1, set_frutas2)
    frutas_solo_en_frutas2 = encontrar_frutas_solo_en_frutas2(set_frutas1, set_frutas2)

    print("Frutas comunes:", frutas_comunes)
    print("Frutas solo en frutas1:", frutas_solo_en_frutas1)
    print("Frutas solo en frutas2:", frutas_solo_en_frutas2)
