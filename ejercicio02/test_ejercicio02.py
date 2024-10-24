from ejercicio02 import formula

# Prueba para comprobar que devuelve el dato faltante, al ser las primeras pruebas no calculé el resultado por lo que
# las pruebas se veían así

# def test_formula_D_T():
#     assert formula('D=32', 'T=4') == 'V'

def test_formula_D_T():
    assert formula('D=32', 'T=4') == 'V=8'

def test_formula_T_D():
    assert formula('T=4', 'D=32') == 'V=8'

def test_formula_D_V():
    assert formula('D=32', 'V=8') == 'T=4'

def test_formula_V_D():
    assert formula('V=8', 'D=32') == 'T=4'

def test_formula_T_V():
    assert formula('T=4', 'V=8') == 'D=32'

def test_formula_V_T():
    assert formula('V=8', 'T=4') == 'D=32'

def test_formula_D100_T20():
    assert formula('d=100', 't=20') == 'V=5'

def test_formula_v50_t2():
    assert formula('V=50', 't=2') == 'D=100'

def test_formula_d150_v30():
    assert formula('d=150', 'v=30') == 'T=5'

def test_formula_t10_v60():
    assert formula('T=10', 'V=60') == 'D=600'