def cambio(texto, num):
    letras = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
        'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
    )

    cipherText = ''

    for letra in texto:
        index = letras.index(letra)

        print((letras.index(letra) + num) % len(letras))

    return cipherText


