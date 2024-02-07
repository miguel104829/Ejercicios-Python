def combine_gradations(*gradations):
    combined = []
    for gradation in gradations:
        combined.extend(gradation)
    combined.sort()
    return combined

def meets_standard(combined, standard):
    # Aquí debes definir cómo se verifica si la granulometría combinada cumple con la norma
    # Este es solo un ejemplo
    return all(s in combined for s in standard)

# Representa diferentes tamaños de materiales granulares
sand = [0.0625, 0.125, 0.25, 0.5, 1.0]
gravel = [1.0, 2.0, 4.0, 8.0, 16.0]

# Combina y ordena las gradaciones
combined = combine_gradations(sand, gravel)

# Define una norma
standard = [0.0625, 0.125, 0.25, 0.5, 1.0, 2.0, 4.0, 8.0, 16.0]

# Verifica si la granulometría combinada cumple con la norma
if meets_standard(combined, standard):
    print("La granulometría combinada cumple con la norma")
else:
    print("La granulometría combinada no cumple con la norma")