def convertir_a_ascii(texto):
    numeros_ascii = []
    for letra in texto:
        numero_ascii = ord(letra)
        numeros_ascii.append(numero_ascii)
    return numeros_ascii

texto = input()
numeros_ascii = convertir_a_ascii(texto)
print(' '.join(map(str, numeros_ascii)))
