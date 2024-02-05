import time
import random

def cyclic_sort(nums):
    for i in range(len(nums)):
        while nums[i] - 1 != i:
            j = nums[i] - 1
            nums[i], nums[j] = nums[j], nums[i]
    return nums

# Genera una lista de longitud 21 con números únicos en el rango de 1 a 21
n = 1000
nums = random.sample(range(1, n+1), n)

start_time = time.perf_counter()
cyclic_sort(nums)
end_time = time.perf_counter()

print(f"Lista ordenada: {nums}")
print(f"Tiempo de ejecución: {(end_time - start_time) * 1000} milisegundos")