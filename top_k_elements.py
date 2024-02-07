def top_k_elements(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
    
    # Return the top k elements
    return arr[:k]

# Test the function
arr = [4, 2, 9, 7, 5, 1, 6, 3, 8]
k = 3
top_k = top_k_elements(arr, k)
print(f"The top {k} elements are: {top_k}")