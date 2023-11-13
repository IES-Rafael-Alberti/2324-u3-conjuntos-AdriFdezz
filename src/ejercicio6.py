#Dado el conjunto de letras:

#vocales = {'a', 'e', 'i', 'o', 'u'}
#Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
#Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.

def obtener_conjuntos_letras():
    """
    Realiza operaciones con conjuntos a partir de un conjunto dado de vocales.

    Retorna:
    - set: Conjunto de consonantes.
    - set: Conjunto de letras comunes entre vocales y consonantes.
    """
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabeto = set('abcdefghijklmnopqrstuvwxyz')
    consonantes = alfabeto - vocales
    letras_comunes = vocales.intersection(consonantes)

    return consonantes, letras_comunes

if __name__ == "__main__":
    consonantes_resultado, letras_comunes_resultado = obtener_conjuntos_letras()

    print("Conjunto de consonantes:", consonantes_resultado)
    print("Conjunto de letras comunes:", letras_comunes_resultado)
