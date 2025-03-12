

x = 10
# - class int
# print(type(x))
# - Immutable
# - No-limit.
# print(2 **64 - 1)
x = 2**512
# print(x)

# float - decimal point
x = 3.14
print(type(x))
# - Immutable.
# double -precision.
x = 1.2e4 # 1.2 * 10^4
print(x)
x = 1.2e-4 # 1.2 / 10^4
print(x)

# complex -  x + yj
# Mutable / Immutable.

x = 10
x = x + 1
# Text data - UNICODE.
# class str - immutable
x = 'test'
x = "test"
x = """test"""
x = "dad's car"

# list - mutable. list,
# [] -
my_list = [1, 2, 3,4]
my_list = []
my_list = ["a", 1, 2, 3.4, [11, 22]]

# tuple - class tuple. immutable
# ()
my_tup = (1, 2, 3)
my_tup = ()
my_tup = (1,)
my_tup = (1, "A", 3.4, (1, 2, 3), [11, 12])

#Set - class set. {}. mutable
# elemets must be immutable
# unique
my_set = {1, 2, 3, 4, 5, 6, 6, 6, 6}
print(my_set)
my_set = set()

# dict. Mutable. Key:value
my_dict = {1: "AA", "22": [1, 2,3]}
# keys - immutable
# value - data type
print(my_dict[1])

# boolean - true or false. immutable. class bool.
is_filled = True

# byte and bytearray - binary data.
# class byte; class bytearray.

# NoneType - absence of value.
x = None # Class NonType.

