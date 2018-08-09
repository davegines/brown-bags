degrees_celsius = [20, 25, 30, 35]


# convert the array of degrees_celsius to fahrenheit
def convert_celsius_to_fahrenheit():
    m = map(lambda c: celsius_to_fahrenheit(c), degrees_celsius)
    return list(m)


# return a filtered list from the degrees_celsius array that are greater than 26
def filtered_list():
    f = filter(lambda x: x > 26, degrees_celsius)
    return list(f)


# convert the array to fahrenheit (from problem #1) then filter out those less than 80 degrees fahrenheit
def greater_than_80_degrees_fahrenheit():
    m = filter((lambda far: far >= 80), map(lambda c: celsius_to_fahrenheit(c), degrees_celsius))
    return list(m)


# find the intersection of list 'a' and 'b'
def intersection():
    a = [1, 2, 3]
    b = [2, 3, 4]
    i = filter(lambda x: x in a, b)
    return list(i)


# helper methods
def celsius_to_fahrenheit(celsius):
    return celsius * 1.8 + 32


print('\n*** celsius to fahrenheit ***')
print(convert_celsius_to_fahrenheit())

print('\n*** filtered list ***')
print(filtered_list())

print('\n*** greater than 80 degrees fahrenheit ***')
print(greater_than_80_degrees_fahrenheit())

print('\n*** intersection ***')
print(intersection())
