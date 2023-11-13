from src.ejercicio3 import conjunto_potencia

def test_distinct_elements():

    input_set = {6, 1, 4}
    
    result = conjunto_potencia(input_set)
    
    assert result == [set(), {1}, {4}, {1, 4}, {6}, {1, 6}, {4, 6}, {1, 4, 6}]
