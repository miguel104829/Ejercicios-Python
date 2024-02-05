import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage

for n in [1000]:
    nums = [random.randint(0, 100) for _ in range(n)]
    start_time = time.perf_counter()
    sorted_nums = merge_sort(nums)
    end_time = time.perf_counter()
    print(f"Lista ordenada para n = {n}: {sorted_nums}")
    print(f"Tiempo de ejecución para n = {n}: {(end_time - start_time) * 1000} milisegundos")
