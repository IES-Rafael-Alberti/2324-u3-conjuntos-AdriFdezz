from src.ejercicio5 import operaciones_con_conjuntos

def test_operaciones_con_conjuntos():
    numeros = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    pares_esperados = {2, 4, 6, 8, 10}
    multiplos_de_tres_esperados = {3, 6, 9}
    interseccion_esperada = {6}

    resultados = operaciones_con_conjuntos(numeros)

    assert resultados[0] == pares_esperados
    assert resultados[1] == multiplos_de_tres_esperados
    assert resultados[2] == interseccion_esperada