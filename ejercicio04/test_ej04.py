from ejercicio04 import kaprekar

def test_kap6174():
    assert kaprekar('6174') == 0

def test_kap0000():
    assert kaprekar('0000') == 8

def test_kap1111():
    assert kaprekar('1111') == 8

def test_kap0009():
    assert kaprekar('0009') == 4

def test_kap3524():
    assert kaprekar('3524') == 3

def test_kap1121():
    assert kaprekar('1121') == 5

def test_kap1893():
    assert kaprekar('1893') == 7

def test_kap3962():
    assert kaprekar('3962') == 6

def test_kap1():
    assert kaprekar('1') == 5
