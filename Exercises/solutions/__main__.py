'''Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.'''
def adjacent_elements_product(input_array):
    largest_product = -99999
    index = 0
    while index < len(input_array) - 1:
        product = input_array[index] * input_array[index + 1]
        largest_product = product if product > largest_product else largest_product
        index += 1
    return largest_product if largest_product != -99999 else None

print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))  # expect result = 21
print(adjacent_elements_product([1, -2, 2]))  # expect result = -2
print(adjacent_elements_product([1]))  # expect result = None


def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('dad'))  # expect True
print(is_palindrome('Max'))  # expect False
