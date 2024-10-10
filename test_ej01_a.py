from ejercicios import cambio

def test_cambio10():
    assert cambio('a', 10) == 'k'

def test_cambio8():
    assert cambio('g', 8) == 'ñ'

def test_cambio2():
    assert cambio('amaro', 2) == 'cñctq'

def test_cambio3():
    assert cambio('hola', 3) == 'krñd'