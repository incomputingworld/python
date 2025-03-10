# Tuples - (), tuple()
""""""
# tup = (1, 2, 3, 4, 5)
# empty_tup = ()
# single_elm_tup = (1,)
# print(type(single_elm_tup))
# single_elm_tup = (11)
# print(type(single_elm_tup))


# Characteristics
# Ordered.
# Immutable.
# Supports duplicate values.
# Heterogeneous.
# hetero_tup = (1, "abc", 2.4, [11, 12, 13])
# print(hetero_tup)
# list_from_tup = hetero_tup[3]
# list_from_tup[0] = 111
# list_from_tup.remove(12)
# list_from_tup.append(500)
# print(hetero_tup)

# Traversal and slicing
"""
Indexing
Use an index in square bracket [] to access an individual element.
If you mention an out of range index, It throws IndexError exception
Tuple supports both positive and negative indexing.
"""
# my_tup = tuple("In Computing World")
# print(my_tup)
# print(f"my_tup[3] - {my_tup[3]}")  # Outputs - C
# print(f"my_tup[3] - {my_tup[-15]}")  # Outputs - C
# # print(f"my_tup[3] - {my_tup[31]}")  # Outputs - IndexError exception

"""
Slicing
Use square bracket [] to mention start, end and step values.
    start - is the starting index. When not mentioned 0 is the default value.
    end - is the ending index (exclusive). When not mentioned, count of elements is the
    default value
    step - Number of characters to skip after extracting first character. 
    Default value is 1. Means extract all the characters.
"""

# my_tup = tuple("In Computing World")
# print(f"my_tup[:] - {my_tup[:]}")  # Outputs - all elements of tuple
# print(f"my_tup[3:12] - {my_tup[3:12]}")  # Outputs - Computing
# print(f"my_tup[3:12:2] - {my_tup[3:12:2]}")  # Outputs - Cmuig

"""
Slicing - starting index bigger than ending index
When start index is bigger than or equals to the end index, in that case the 
  slicing operation returns an empty object.
"""
# my_tup = tuple("In Computing World")
# print(f"my_tup[11:2] - {my_tup[11:2]}")  # Outputs empty tuple
# print(f"my_tup[20:4:] - {my_tup[20:4:]}")  # Outputs empty tuple


"""
Slicing - Negative Indexing
When negative values are mentioned in start and end, Python converts the negative 
  values to positive values. It does this by adding the count of elements to the
  negative index value.
"""
# my_tup = tuple("In Computing World")
# print(f"my_tup[-15:-6] - {my_tup[-15:-6]}")  # Outputs - Computing
# # -15 + 18 = 3 (18 = count of elements in this tuple)
# # -6 + 18 = 12
# # my_tup[-15:-6] same as my_tup[3:12]


"""
Slicing - Negative Step value
When start index is bigger than the end index and step value is mentioned in 
  negative, in that case the slicing returns elements in reverse order.  
"""
# my_tup = tuple("In Computing World")
# print(f"my_tup[11:2:-1] - {my_tup[11:2:-1]}")  # Outputs gnitupmoC
# print(f"my_tup[::-1] - {my_tup[::-1]}")  # OOutputs dlroW gnitupmoC nI
# print(f"my_tup[::-1] - {my_tup[3:12:-2]}")  # OOutputs - empty tuple


# Accessing and Indexing
"""
index(element) - This function returns the index of the first occurrence of the given
  element. If the element does not exist, it throws ValueError exception.

count(element) - returns the number of times a given element exist in the tuple.
  If the value does not exist, it returns 0.
  
To check if an element exists in a tuple or not... 
in - this operator returns true when the given element exists in a tuple
not in - this operator returns true when the given element does not exist in a tuple
"""

# hetero_tup = (1, "abc", 2.4, [11, 12, 13])
# print(f"hetero_tup.index(2.4) - {hetero_tup.index(2.4)}")  # Outputs - 2
# # print(f"hetero_tup.index(11) - {hetero_tup.index(11)}")  # Outputs - ValueError Exception
#
# print(f"hetero_tup.count(2.4) - {hetero_tup.count(2.4)}")  # Outputs - 1
# print(f"hetero_tup.count(11) - {hetero_tup.count(11)}")  # Outputs - 0
#
# print(f"2.4 in hetero_tup - {2.4 in hetero_tup}")  # Outputs - True
# print(f"11 not in hetero_tup - {11 not in hetero_tup}")  # Outputs - True


# Tuple Operations
"""
len() - use this function to count the number of elements in a tuple.

sorted() - use this function to sort the elements of a tuple. This function returns
  a list of sorted elements.
  In case the tuple contains incompatible data types (like string and numbers) in that
  the sorted function will fail.
"""

# hetero_tup = (1, "abc", 2.4, [11, 12, 13])
# print(len(hetero_tup))  # Outputs - 4
# tup = (3, 2, 5, 6, 3, 4, 7)
# sorted_tup = sorted(tup)
# print(type(sorted_tup), sorted_tup)  # Outputs - <class 'list'> [2, 3, 3, 4, 5, 6, 7]


# Packing and unpacking
"""
Packing allows to assign multiple values to a tuple. Another way of defining a tuple
without using the parentheses.

Unpacking allows to assign each variable a value from a tuple.
While unpacking, if the number of variables is less than the values in a tuple, in that
case use * before one variable. This variable will catch all the extra values in the 
form of a list.
You can put * to any variable to gather the remaining values of a tuple.
"""
# Packing example
a = 10
b = 20
c = 30
d = 40
numbers = a, b, c, d  # packing
print(f"Packed numbers - {type(numbers)}, {numbers}")

# Unpacking example
*w, x, y = numbers  # unpacking
print(f"w={w}-{type(w)}; x={x}-{type(x)}; y={y}-{type(y)}")




