def double_even_numbers(numbers):
    result = numbers
    
    for i in range(len(numbers) + 1):
        if numbers[i] % 2 = 0:
            result[i] = number[i] * 2
            
    return result

# Test case: Should output [2, 4, 3, 8]
sample_list = [1, 4, 3, 4]
print(double_even_numbers(sample_list))