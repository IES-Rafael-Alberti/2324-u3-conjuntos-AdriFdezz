from src.ejercicio2 import mostrar_resultados

def test_mostrar_resultados(capsys):
    nombres_primaria = {'Juan', 'Luis', 'Ana'}
    nombres_secundaria = {'Luis', 'Ana', 'Miguel'}

    mostrar_resultados(nombres_primaria, nombres_secundaria)
    captured = capsys.readouterr()

    assert "Nombres de todos los alumnos de primaria y secundaria sin repeticiones:" in captured.out
    assert "Nombres que se repiten entre primaria y secundaria:" in captured.out
    assert "Nombres de primaria que no se repiten en secundaria:" in captured.out
    assert "¿Todos los nombres de primaria están incluidos en secundaria?" in captured.out
