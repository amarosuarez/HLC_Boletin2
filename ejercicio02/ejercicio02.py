def formula(dato1, dato2):
    # Formulas
    # V = D / T
    # D = V * T
    # T = D / V

    numRes = 0
    res = ''

    d1 = dato1.split('=')[0].upper()
    d2 = dato2.split('=')[0].upper()
    n1 = int(dato1.split('=')[1])
    n2 = int(dato2.split('=')[1])
    
    if ((d1 == 'D' or d1 == 'T') and (d2 == 'D' or d2 == 'T')):
        numRes = int(obtenerValor(d1, d2, n1, n2, 'D') / obtenerValor(d1, d2, n1, n2, 'T'))
        
        res = 'V='
    elif ((d1 == 'D' or d1 == 'V') and (d2 == 'D' or d2 == 'V')):
        numRes = int(obtenerValor(d1, d2, n1, n2, 'D') / obtenerValor(d1, d2, n1, n2, 'V'))

        res = 'T='
    else:
        numRes = n1 * n2

        res = 'D='

    return res + str(numRes)

# He creado esta función para no hacer un ternario
def obtenerValor(d1, d2, n1, n2, obj):
    ret = n1

    if d2 == obj:
        ret = n2
    
    return ret
