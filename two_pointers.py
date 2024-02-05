def two_pointers(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
result = two_pointers(nums, target)
print(result)
