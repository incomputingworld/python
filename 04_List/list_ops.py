# List -
# Creating a list
# my_list = [1, 2, 3]
# empty_list = []
# my_list1 = [1, "a", 3.14, [11, 12]]
""""""
# Characteristics of a list
# Mutable example
# my_list = [1, 2, 3]
# print(id(my_list))
# print(my_list)
# my_list.append(4)
# print(id(my_list))
# print(my_list)
#
# # Hetrogeneous and nesting example
# my_list1 = [1, 1, "abc", 3.14, [11, 12]]

# Add and remove element(s)
"""
Add methods -
append(element) - adds a new element at the end of the list
insert(index, element) - add a new element at the given index
extend(iterable) - adds all the elements of an iterable at the end
    of the list.
"""
# numbers = [1, 2, 3, 4]
# print(f"Initial list - {numbers}")
# numbers.append(5)
# print(f"append(5) - {numbers}")  # outputs - [1, 2, 3, 4, 5]

# numbers.insert(0, 0)
# print(f"insert(0, 0) - {numbers}")  # outputs - [0, 1, 2, 3, 4, 5]
# numbers.insert(10, 7)
# print(f"insert(10, 7) - {numbers}")  # outputs - [0, 1, 2, 3, 4, 5, 7]

# more_nums = [7, 8, 9, 10]
# numbers.extend(more_nums)
# print(numbers)  # outputs - [0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 10]

# Add and remove element(s)
"""
Remove methods -
pop([index]) - removes the element mentioned at the given index.
    When index is not mentioned, pop removes the last element of the list.
    The function returns the removed value. In case of invald index value
    this function throws an IndexError exception.
remove(element) - removes the first matching element. If the element
    does not exist, the function throws a ValueError exception.
clear() - deletes all the elements of a list.
"""
# numbers = [0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 10]
# print(f"Initial list - {numbers}")  # Outputs - [0, 1, 2, 3, 4, 5, 7, 7, 8, 9, 10]
# print(f"Removed last element - {numbers.pop()}")  # Outputs -  Removed last element - 10
# print(numbers) # Outputs - [0, 1, 2, 3, 4, 5, 7, 7, 8, 9]
# print(f"Removed (0th) element - {numbers.pop(0)}")  # Outputs - Removed (0th) element - 0
# print(numbers)  # Outputs - [1, 2, 3, 4, 5, 7, 7, 8, 9]
# # print(f"pop with invalid index - {numbers.pop(21)}") # throws IndexError exception
# # print(numbers)
# print(f"Removed element (7) - numbers.remove(7)")
# numbers.remove(7)
# print(numbers)  # Outputs - [1, 2, 3, 4, 5, 7, 8, 9]
#
# # print(f"Remove element(15) - {numbers.remove(15)}")  # throws ValueError exception
# # print(numbers)
# print(f"clear() - delete all elements.")
# numbers.clear()
# print(numbers)  # Outputs - []

# Traversal and slicing
"""
Can access an element of a list using an index. We can use both 
positive and negative index. Index is mentioned within square bracket - []

Slicing - used to extract one or more elements of a list. 
Use the square bracket - []. Exptect values within these brackets
[start: end: step] - these values are segregated uing colon
start - is the starting index
end - ending index (exlcusive)
step - number of characters to skip after getting the first character.
"""






# my_list = list("In Computing World")
# print(my_list)

# Extracting individual element
# print(f"my_list[0] - {my_list[0]}")  # Outputs - I
# print(f"my_list[17] - {my_list[17]}")  # Outputs - d
# print(f"my_list[17] - {my_list[-1]}")  # Outputs - d
# print(f"my_list[17] - {my_list[-18]}")  # Outputs - I
# # print(f"my_list[17] - {my_list[20]}")  # Outputs - IndexError exception
# # print(f"my_list[17] - {my_list[-20]}")  # Outputs - IndexError exception




# my_list = list("In Computing World")
# # Read complete list all the statements give the following output
# # ['I', 'n', ' ', 'C', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g', ' ', 'W', 'o', 'r', 'l', 'd']
# print(f"my_list[:] - {my_list[:]}")
# print(f"my_list[0:] - {my_list[0:]}")
# print(f"my_list[:18] - {my_list[:18]}")
# print(f"my_list[:20] - {my_list[:20]}")  # throws no error





# my_list = list("In Computing World")
# print(my_list)
# print(f"my_list[3:12] - {my_list[3:12]}")  # Outputs- ['C', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g']
# print(f"my_list[3:12:2] - {my_list[3:12:2]}")  # Outputs - ['C', 'm', 'u', 'i', 'g']
# print(f"my_list[3:12:3] - {my_list[3:12:3]}")  # Outputs - ['C', 'p', 'i']
# print(f"my_list[4:4] - {my_list[4:4]}")  # Outputs - []
# print(f"my_list[20:4] - {my_list[20:4]}")  # Outputs - []
# print(f"my_list[5:4] - {my_list[5:4]}")  # Outputs - []





# my_list = list("In Computing World")
# print(f"my_list[-1:] - {my_list[-1:]}")  # Outputs -  [d]
# print(f"my_list[-18:] - {my_list[-18:]}")  # Outputs -  In Computing World
# print(f"my_list[-18:-1:] - {my_list[-18:-1]}")  # Outputs -  In Computing Worl
# print(f"my_list[:-18]) - {my_list[:-18]}")  # Outputs -  empty list
# print(f"my_list[-15:-6] - {my_list[-15:-6]}")  # Outputs -  Computing
# print(f"my_list[-1: -10] - {my_list[-1: -10]}")  # Outputs -  empty list
# my_list[17:] - -1 + 18 = 17
# my_list[0:] - 18 + 18 = 0
# my_list[0:17] -
# my_list[:0] -
# my_list[3:12] -
# my_list[17:8] -




# my_list = list("In Computing World")
# print(f"my_list[-15:-6: 2] - {my_list[-15:-6: 2]}")  # Outputs -  Cumig
# print(f"my_list[-15:-6: -2] - {my_list[-15:-6: -2]}")  # Outputs -  empty list
# print(f"my_list[-6:-15: -2] - {my_list[-6:-15: -2]}")  # Outputs -   ntpo
#
# print(f"my_list[11:2:-1] - {my_list[11:2:-1]}")  # outputs gnitupmoC
# print(f"my_list[::-1] - {my_list[::-1]}")  # outputs dlroW gnitupmoC nI
# my_list[3: 12: 2]
# my_list[3: 12: -2]
# my_list[12: 2: -2]
# my_list[11: 2: -1]
# my_list[::-1]


# Search and Find
"""
index(element, start, end) - Searches for the first occurance of the element.
    When found, returns the index of the element, otherwise throws ValueError exception.
    start and end are optional parameters. These define the starting and ending index
    to search for a value.

count(element) - returns the count of occurance of an element in the list.
    If the element does not exist, the function returns 0
    
IN and NOT IN menbership operator
    IN returns true when an element exists in a list. 
    NOT IN returns true when an element does not exist in a list.
"""


# my_list = list("In Computing World")
# print(my_list)
# print(f"my_list.index('o') - {my_list.index('o')}")  # outputs - 4
# print(f"my_list.index('o', 5) - {my_list.index('o', 5)}")  # outputs - 14
# # print(my_list.index('O'))  # throws ValueError exception
# print(f"my_list.count('o') - {my_list.count('o')}")  # outputs - 2
# print(f"my_list.count('Oo') - {my_list.count('Oo')}")  # outputs - 0
# print(f"'d' in my_list - {'d' in my_list}")  # outputs - True
# print(f"'D' not in my_list - {'D' not in my_list}")  # outputs - True




# Sort and Reverse
"""
reverse() - reverses the elements of a list. 

reversed(sequence) - returns an iterable "list_reverseiterator". This allows to access 
    the elements of a list (sequence) in reverse order. This does not reverse the list.
    
sort(key, reverse) - sorts a list in ascending order. Default functionality. reverse = False
    Set reverse = True to sort list in descending order.
    key - refers to a function that we can use to define our own sorting order.
    
sorted(iterable, key, reverse) - Works same as sort(). This function creates a new sorted
    list and returns it. Does not modify the list we pass to this function (iterable)
"""


# numbers = [3, 1, 4, 2, 6, 5]
# reverse()
# print(f"numbers before reverse - {numbers}")  # Outputs - [3, 1, 4, 2, 6, 5]
# numbers.reverse()  # In place reverse
# print(f"numbers afer reverse - {numbers}")  # Outputs - [5, 6, 2, 4, 1, 3]


# numbers = [3, 1, 4, 2, 6, 5]
# reversed()
# print(f"numbers before reversed() - {numbers}")  # outputs - [3, 1, 4, 2, 6, 5]
# num_iter = reversed(numbers)  # returns reverse list iterator
# print(f"numbers after reversed() - {numbers}")  # Outputs - [3, 1, 4, 2, 6, 5]
# print(type(num_iter))  # Outputs - <class 'list_reverseiterator'>
# print(next(num_iter), next(num_iter), next(num_iter))  # Outputs - 5 6 2
# print(next(num_iter), next(num_iter), next(num_iter))  # Outputs - 4 1 3





# numbers = [3, 1, 4, 2, 6, 5]
# Sort() - on numbers
# print(f"numbers before sorting - {numbers}")  # outputs - [3, 1, 4, 2, 6, 5]
# numbers.sort()  # In place sorting
# print(f"numbers after sorting-Asc order - {numbers}")  # outputs - [1, 2, 3, 4, 5, 6]
# numbers.sort(reverse=True)  # In place sorting
# print(f"numbers after sorting-Desc order - {numbers}")  # outputs - [6, 5, 4, 3, 2, 1]



# fruits = ['apple', 'banana', 'pineapple', 'strawberry', 'apricot']
# print(f"fruits - {fruits}")  # - ['apple', 'banana', 'pineapple', 'strawberry', 'apricot']
# fruits.sort(reverse=True)
# print(f"fruits sorted - {fruits}")  # - ['strawberry', 'pineapple', 'banana', 'apricot', 'apple']
# fruits.sort(key=len)
# print(f"fruits sorted on length - {fruits}")  # - ['apple', 'banana', 'apricot', 'pineapple', 'strawberry']





# numbers = [3, 1, 4, 2, 6, 5]
# sorted_nums = sorted(numbers)
# print(f"numbers - {numbers}")  # Outputs - [3, 1, 4, 2, 6, 5]
# print(f"Sorted numbers - {sorted_nums}")  # Outputs - [1, 2, 3, 4, 5, 6]




# In place editing
my_list = list("In Computing")
print(my_list)  # Outputs - ['I', 'n', ' ', 'C', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g']
my_list[1] = 'N'
print(my_list)  # Outputs - ['I', 'N', ' ', 'C', 'o', 'm', 'p', 'u', 't', 'i', 'n', 'g']

my_list[3:12] = "COMPUTING"  # replace 9 existing elements by 9 new elements
print(my_list)  # Outputs - ['I', 'N', ' ', 'C', 'O', 'M', 'P', 'U', 'T', 'I', 'N', 'G']
my_list[3:10] = "comp"  # replace 7 existing elements by 4 new elements
print(my_list)  # Outputs - ['I', 'N', ' ', 'c', 'o', 'm', 'p', 'N', 'G']
my_list[3:10] = "COMPUTERISE"  # replace 7 existing elements by 11 new elements
print(my_list)  # Outputs - ['I', 'N', ' ', 'C', 'O', 'M', 'P', 'U', 'T', 'E', 'R', 'I', 'S', 'E']








