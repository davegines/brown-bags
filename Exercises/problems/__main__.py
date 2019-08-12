'''Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
adjacentElementsProduct(inputArray) = 21.

7 and 3 produce the largest product.'''
def adjacent_elements_product(input_array):
    return None

print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))  # expect result = 21
print(adjacent_elements_product([1, -2, 2]))  # expect result = -2
print(adjacent_elements_product([1]))  # expect result = None


'''Return whether or not a word is a palindrome...it is spelled the same forwards and backwards'''
def is_palindrome(word):
    return True

print(is_palindrome('dad'))  # expect True
print(is_palindrome('Max'))  # expect False



'''Given two strings, return whether or not they are anagrams'''
def are_anagrams(word_1, word_2):
    return True

print(are_anagrams('listen', 'silent'))  # expect True
print(are_anagrams('dog', 'cat'))  # expect False
