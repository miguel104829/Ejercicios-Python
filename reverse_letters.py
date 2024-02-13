def reverse_letters(chars):
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
        
    return chars
print(reverse_letters(['a', 'b', 'c', 'd', 'e'])) 
