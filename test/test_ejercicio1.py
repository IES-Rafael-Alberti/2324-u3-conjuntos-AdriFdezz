from src.ejercicio1 import domicilios_factura

def test_domicilios_facturas():
    compras = [('Cliente1', 1, 100, 'Direccion1'), ('Cliente2', 2, 200, 'Direccion2'), ('Cliente3', 3, 300, 'Direccion3')]
    assert set(domicilios_factura(compras)) == set(['Direccion1', 'Direccion2', 'Direccion3'])