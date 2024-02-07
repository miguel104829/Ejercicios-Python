def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        # Si x está presente en el medio
        if arr[mid] < x:
            low = mid + 1
 
        # Si x es mayor, ignora la mitad izquierda
        elif arr[mid] > x:
            high = mid - 1
 
        # Si x es menor, ignora la mitad derecha
        else:
            return mid
 
    # Si no encontramos el elemento
    return -1
 
 
# Lista de prueba
arr = [2, 3, 4, 10, 40]
x = 10
 
# Función de llamada
result = binary_search(arr, x)
 
if result != -1:
    print("El elemento está presente en el índice", str(result))
else:
    print("El elemento no está presente en el array")