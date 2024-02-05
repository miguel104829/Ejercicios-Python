import time
import random

def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]  # swap
        else:
            i += 1
    return nums

# Genera una lista de longitud 21 con números únicos en el rango de 1 a 21
n = 100
nums = random.sample(range(1, n+1), n)

start_time = time.perf_counter()
cyclic_sort(nums)
end_time = time.perf_counter()

print(f"Lista ordenada: {nums}")
print(f"Tiempo de ejecución: {(end_time - start_time) * 1000} milisegundos")