def bitwise_xor(a, b):
    result = a ^ b
    return result

# Example usage
num1 = 10
num2 = 7
xor_result = bitwise_xor(num1, num2)
print(f"The XOR of {num1} and {num2} is: {xor_result}")
# Example usage with list
nums = [10, 7, 5, 3]
xor_result = nums[0]
for num in nums[1:]:
    xor_result ^= num
print(f"The XOR of {', '.join(map(str, nums))} is: {xor_result}")