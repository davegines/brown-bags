data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print the first 3 items
print(data[:3])

# print the last 3 items
print(data[-3:])

# print the middle 2 items
print(data[4:6])

# print every other item backwards
print(data[::-2])

# BONUS: find the total of all the even numbers in the array
print(sum([d for d in data[1::2]]))
