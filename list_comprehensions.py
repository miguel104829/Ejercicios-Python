def generate_coordinates(n):
    return [(i, j, k) for i in range(n+1) for j in range(n+1) for k in range(n+1) if i + j + k != n]

n = int(input("Ingrese el valor de n: "))
resultado = generate_coordinates(n)
print(resultado)