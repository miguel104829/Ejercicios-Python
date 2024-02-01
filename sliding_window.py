def sliding_window(nums, k):
    result = []
    window_sum = sum(nums[:k])
    result.append(window_sum)
    print (result)
    
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        result.append(window_sum)
        print (result)
    
    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window(nums, k)
print(result)
