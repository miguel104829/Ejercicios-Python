import time
def selection_sort(numbers):
    for i in range(len(numbers)):
        min_index = i
        for j in range(i+1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

start_time = time.time()
# Example usage
numbers = [5, 2, 8, 3, 1, 6,10, 7, 4, 9, 0, 20, 15, 12, 11, 18, 19, 17, 13, 14, 16]
sorted_numbers = selection_sort(numbers)
print(sorted_numbers)
end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")  