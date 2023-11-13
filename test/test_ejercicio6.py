from src.ejercicio6 import obtener_conjuntos_letras

def test_obtener_conjuntos_letras():
    consonantes_esperadas = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    letras_comunes_esperadas = set()

    consonantes_resultado, letras_comunes_resultado = obtener_conjuntos_letras()

    assert consonantes_resultado == consonantes_esperadas
    assert letras_comunes_resultado == letras_comunes_esperadas