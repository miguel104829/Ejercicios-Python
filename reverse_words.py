def reverse_words(message):
    # Primero invertimos todos los caracteres en el mensaje completo
    reverse_characters(message, 0, len(message)-1)

    # Esto nos da el orden correcto de las palabras
    # pero con cada palabra al revés

    # Ahora haremos que las palabras estén hacia adelante nuevamente
    # invirtiendo los caracteres de cada palabra

    # Mantenemos el índice del *inicio* de la palabra actual
    # mientras buscamos el *fin* de la palabra actual
    current_word_start_index = 0

    for i in range(len(message) + 1):
        # ¡Encontramos el final de la palabra actual!
        if (i == len(message)) or (message[i] == ' '):
            reverse_characters(message, current_word_start_index, i - 1)
            # Si no hemos agotado el mensaje, el inicio de nuestra próxima palabra es un carácter adelante
            current_word_start_index = i + 1


def reverse_characters(message, left_index, right_index):
    # Avanzamos hacia el centro, desde ambos lados
    while left_index < right_index:
        # Intercambiamos el carácter izquierdo y el carácter derecho
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index += 1
        right_index -= 1

# Ejemplo de uso:
message = list([ 'l', 'a', 'n', 'd', 'e', 'd', ' ', 'h', 'a', 's', ' ',
  'e', 'a', 'g', 'l', 'e', ' ', 't', 'h', 'e' ])
reverse_words(message)
print(''.join(message))
