import collections


'''rotate 2 dimensional array 90 degrees clockwise'''
def rotate(two_dimensional_array):
    array_items_count = len(two_dimensional_array)
    new_array = []
    x = 0
    while x < array_items_count:
        sub_array = ''
        y = array_items_count - 1
        while y >= 0:
            sub_array += str(two_dimensional_array[y][x])
            if y > 0:
                sub_array += ', '
            y -= 1
        new_array.append([sub_array])
        x += 1
    return new_array


print(rotate([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]))


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


# print(adjacent_elements_product([3, 6, -2, -5, 7, 3]))  # expect result = 21
# print(adjacent_elements_product([1, -2, 2]))  # expect result = -2
# print(adjacent_elements_product([1]))  # expect result = None


'''Given two strings, return whether or not they are anagrams'''
def are_anagrams(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok
