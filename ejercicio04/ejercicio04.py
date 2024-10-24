def kaprekar(num):
    kap = 0

    repdigits = True

    if num != '6174':
        # Comprueba si el número tiene menos de 4 digitos y le añade tantos 0 a la izquierda como digitos falten
        while len(num) < 4:
            num = '0' + str(num)

        #Primer digito
        d1 = num[0]

        for n in num:
            if d1 != n:
                repdigits = False
                break
            d1 = n
        
        if repdigits:
            kap = 8
        else:
            # Si tiene menos de 4 dígitos se le añade tantos 0 a la izquierda como digitos falten
            res = str(num)

            while res != '6174' and kap < 7:  
                # Ordeno el numero de mayor a menor y viceversa
                li = list(str(res))
                li2 = li.copy()

                # Orden descendente
                li.sort(reverse=True)

                # Orden ascendente
                li2.sort() 

                n1 = int(''.join(li))  
                n2 = int(''.join(li2))  

                res = n1 - n2

                # Si el resultado de la resta tiene menos de 4 dígitos se le añade tantos 0 a la izquierda como digitos falten
                while len(str(res)) < 4:
                    res = '0' + str(res)

                res = str(res)
                kap += 1  

    return kap
