#Itera sobre la lista de colores y muestra en la consola con el método format, 
# se muestra en lista con guiones y puntos
colors = ["red", "green", "blue", "yellow"]
GUION = "-"
PUNTO = "."

for color in colors:
    print("{}{}{}".format(GUION,color.capitalize(), PUNTO))
