def generate_subsets(nums):
    subsets = [[]]  # Start with an empty subset
    for num in nums:
        new_subsets = []
        for subset in subsets:
            new_subsets.append(subset + [num])  # Add the current number to each existing subset
        subsets.extend(new_subsets)  # Add the new subsets to the existing ones
    return subsets

# Example usage
nums = [1, 2, 3]
result = generate_subsets(nums)
print(result)