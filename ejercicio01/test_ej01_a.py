from ejercicio01 import cambio

def test_cambio10():
    assert cambio('a', 10) == 'k'

def test_cambio8():
    assert cambio('g', 8) == 'ñ'

def test_cambio2():
    assert cambio('amaro', 2) == 'cñctq'

def test_cambio3():
    assert cambio('hola', 3) == 'krñd'

def test_cambio4():
    assert cambio('zeba', 4) == 'dife'

def test_cambio8():
    assert cambio('zwirt', 8) == 'hepzb'

def test_cambio_espacio():
    assert cambio('za c', 1) == 'ab d'

def test_cambio_espacio_coma():
    assert cambio('za c, a', 1) == 'ab d, b'