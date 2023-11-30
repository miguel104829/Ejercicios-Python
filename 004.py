# Solicitar al usuario que ingrese una letra
letra = input("Ingrese una letra: ")

# Solicitar al usuario que ingrese una cadena de texto
texto = """Muy lejos, más allá de las montañas de palabras, alejados de los países de las vocales y las consonantes,
viven los textos simulados. Viven aislados en casas de letras, en la costa de la semántica, un gran océano de lenguas.
Un riachuelo llamado Pons fluye por su pueblo y los abastece con las normas necesarias. 
Hablamos de un país paraisomático en el que a uno le caen pedazos de frases asadas en la boca. 
Ni siquiera los todopoderosos signos de puntuación dominan a los textos simulados; una vida, se podría decir, poco natural. 
Si una línea de texto simulado se queda sin hacer nada, pronto cae enferma de aburrimiento y muere de inanición. 
No es de extrañar que sus parientes vivan lejos de ellos, en el valle de la gramática, a lo largo de las montañas de las letras, 
a caballo de la sílaba más consonante y la sílaba más vocálica. Un día, sin embargo, una pequeña línea de texto simulado, 
llamada Lorem Ipsum, decidió aventurarse hacia el mundo amplio de la gramática."""

# Inicializar el contador
contador = 0

# Recorrer cada carácter de la cadena de texto
for caracter in texto:
    # Comparar cada carácter con la letra ingresada
    if caracter == letra:
        # Incrementar el contador en 1
        contador += 1

# Mostrar el resultado
print(f"El número de coincidencias de la letra '{letra}' en el texto es: {contador}")
