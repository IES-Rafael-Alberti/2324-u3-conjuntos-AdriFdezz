from src.ejercicio4 import obtener_conjuntos, encontrar_frutas_comunes, encontrar_frutas_solo_en_frutas1, encontrar_frutas_solo_en_frutas2

def test_obtener_conjuntos():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    set_frutas1, set_frutas2 = obtener_conjuntos(frutas1, frutas2)

    assert set_frutas1 == {"manzana", "pera", "naranja", "plátano", "uva"}
    assert set_frutas2 == {"manzana", "pera", "durazno", "sandía", "uva"}

def test_encontrar_frutas_comunes():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

    frutas_comunes = encontrar_frutas_comunes(set_frutas1, set_frutas2)

    assert frutas_comunes == {"manzana", "pera", "uva"}

def test_encontrar_frutas_solo_en_frutas1():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

    frutas_solo_en_frutas1 = encontrar_frutas_solo_en_frutas1(set_frutas1, set_frutas2)

    assert frutas_solo_en_frutas1 == {"naranja", "plátano"}

def test_encontrar_frutas_solo_en_frutas2():
    set_frutas1 = {"manzana", "pera", "naranja", "plátano", "uva"}
    set_frutas2 = {"manzana", "pera", "durazno", "sandía", "uva"}

    frutas_solo_en_frutas2 = encontrar_frutas_solo_en_frutas2(set_frutas1, set_frutas2)

    assert frutas_solo_en_frutas2 == {"durazno", "sandía"}