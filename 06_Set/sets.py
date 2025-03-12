# Sets - {}, set()
""""""
# my_set = {1, 2, 3, 4, 4, 5}
# print(my_set)  # Outputs - {1, 2, 3, 4, 5}
# empty_set = set()
# print(type(empty_set))  # Outputs <class 'set'>
# empty_set = {}
# print(type(empty_set))  # Outputs <class 'dict'>


# Characteristics -
# Unordered.
# Unique elements.
# Mutable.
# Heterogeneous.

# my_set = {1, 2, 3, 4, 4, 5}
# print(my_set)  # Outputs - {1, 2, 3, 4, 5}  - unique elements
#
# my_set = {1, 2, 3, (11, 12)}
# print(my_set)  # Outputs - {(11, 12), 1, 2, 3} - unordered sequence and heterogeneous
#
# my_set.add(6)
# print(my_set)  # Outputs - {1, 2, 3, 6, (11, 12)} - mutable
#
# # my_set = {1, 2, 3, [11, 12]}  # Outputs - TypeError: unhashable type: 'list'


# Add remove methods
"""
add(element) - adds an element to a set. If the element is already present, it is not added.
update(iterable) - adds elements of an iterable to the set.
"""
# my_set = {1, 2, 3, 4, 4, 5}
# print(my_set)  # Outputs - {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)  # Outputs - {1, 2, 3, 4, 5, 6}
# my_set.update('A', 'B', 'C')
# print(my_set)  # Outputs - {1, 2, 3, 4, 5, 6, 'B', 'A', 'C'}




# Add remove methods
"""
remove(element) - removes the element from a set and returns no value.
  If the element does not exist, function throws KeyError exception
discard(element) - removes the element from a set and returns no value.
  If the element does not exist, function throws no error
pop() - removes any item from a set and returns the value. When the set is empty
  the function raises TypeError exception.
clear() - removes all items from a set. Returns no value.
"""

# my_set = {1, 2, 3, 4, 4, 5}
# print(f"my_set.remove(1) - {my_set.remove(1)}")  # Outputs - None
# # print(f"my_set.remove(11) - {my_set.remove(11)}")  # Outputs - KeyError exception
# print(my_set)  # Outputs - {2, 3, 4, 5}
#
# print(f"my_set.discard(3) - {my_set.discard(3)}")  # Outputs - None
# print(f"my_set.discard(11) - {my_set.discard(11)}")  # Outputs - None
# print(my_set)  # Outputs - {2, 4, 5}
#
# print(f"my_set.pop() - {my_set.pop()}")  # Outputs - popped element
# print(my_set)  # Outputs - remaining elements of a set
#
# print(f"my_set.clear() - {my_set.clear()}")  # Outputs - None
# print(my_set)  # Outputs - {}
#
# # print(f"my_set.pop() - {my_set.pop()}")  # Outputs - throws TypeError exception
# # print(my_set)  # Outputs - {}





# Comparison and membership operations
"""
Membership check... 
To check if an element exists in a set or not... 
in - this operator returns true when the given element exists in a set
not in - this operator returns true when the given element does not exist in a set
"""
# my_set = {1, 2, 3, 4, 5}
# print(f"5 in my_set - {5 in my_set}")  # Outputs - True
# print(f"15 not in my_set - {15 not in my_set}")  # Outputs - True



# Comparison and membership operations
"""
Comparison check...
issubset(set2) - returns True if this set is subset of set2. Otherwize returns False. 
  Subset - when all the elements of this set are also the elements of set2.
"""
# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(f"set1.issubset(set2) - {set1.issubset(set2)}")  # Outputs - True
# print(f"set2.issubset(set1) - {set2.issubset(set1)}")  # Outputs - False




# Comparison and membership operations
"""
Comparison check...
issubset(set2) - returns True if this set is subset of set2. Otherwize returns False. 
  Subset - when all the elements of this set are also the elements of set2.

issuperset(set2) - returns True if this set is superset of set2. Otherwize returns False.
  Superset - when the few of the elements of this set are the elements of set2.

isdisjoint(set2) - return True if this set is disjoint of set2. Otherwize returns False.
  Disjoint - when elements of this set do not exist in the elements of set2.
"""

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# set3 = {4, 5}
#
# print(f"set2.issubset(set1) - {set2.issuperset(set1)}")  # Outputs - True
# print(f"set1.isdisjoint(set3) - {set1.isdisjoint(set3)}")  # Outputs - True






# Set operations
"""
union(set2) - This method returns a new set that contains distinct elements of this 
  set and the set2 passed as a parameter. You can use the operator | to find a union
  between two sets. You can pass more than one set as an argument.
"""
# set1 = {1, 2, 3}
# set2 = {4, 5}
# set3 = {5, 6}
# print(f"set1.union(set2, set3) - {set1.union(set2, set3)}")  # Output - {1, 2, 3, 4, 5, 6}
# print(f"set1 | (set2) | set3 - {set1 | set2 | set3}")  # Output - {1, 2, 3, 4, 5, 6}



# Set operations
"""
union(set2) - This method returns a new set that contains distinct elements of this 
  set and the set2 passed as a parameter. You can use the operator | to find a union
  between two sets. You can pass more than one set as an argument.
  
intersection(set2) - This method returns a new set of the elements that are common to
  this set and the set2. You can use the operator & to find an intersection between two sets.
  You can pass more than one set as an argument. In this case common elements from all the 
  sets is returned.
"""
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {3, 6, 7}
# print(f"set1 & set2 - {set1 & set2}")  # Output - {3, 4}
# print(f"set1 & set2 & set3 - {set1 & set2 & set3}")  # Output - {3}



# Set operations
"""
intersection(set2) - This method returns a new set of the elements that are common to
  this set and the set2. You can use the operator & to find an intersection between two sets.
  You can pass more than one set as an argument. In this case common elements from all the 
  sets is returned.
  
intersection_update() - This method works exactly as the intersection function. Instead
  of returning a new set, this function updates the set that calls this function.
"""
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {3, 6, 7}
# # set1.intersection_update(set2)
# # print(f"set1 after intersection_update(set2) - {set1}")  # Output - {3, 4}
# set1.intersection_update(set2, set3)
# print(f"set1 after intersection_update(set2, set3) - {set1}")  # Output - {3}






# Set operations
"""
difference() - Computes the difference between two sets and returns the elements that are 
  unique to the first set. You can also use the operator - to find difference between two
  sets.

difference_update() - This function works exactly as the difference function. Instead
  of returning a new set, this function updates the set that calls this function.
"""

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {3, 6, 7}
# # print(f"set1 - set2 - {set1 - set2}")  # Output - {1, 2}
# # print(f"set2 - set1 - {set2 - set1}")  # Output - {5, 6}
# # print(f"set1 - set2 - set3 - {set1 - set2 - set3}")  # Output - {1, 2}
# set1.difference_update(set2, set3)
# print(f"set1 after difference_update(set2, set3) - {set1}")  # Output - {1, 2}




# Set operations
"""
symmetric_difference(set2) - This function returns elements present in all the sets
  except the common elements of these sets (or the intersection of these sets).
  You can also use the operator ^ to find symmetric difference between two sets.


symmetric_difference_update(set2) - This function works exactly as the 
  symmetric_difference function. Instead of returning a new set, this function 
  updates the set that calls this function.
"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {3, 6, 7}
# print(f"set1 ^ set2 - {set1 ^ set2}")  # Output - {1, 2, 5, 6}
# print(f"set1 ^ set2 ^ set3 - {set1 ^ set2 ^ set3}")  # Output - {1, 2, 3, 5, 7}

set1.symmetric_difference_update(set2)
print(f"set1 after set1.symmetric_difference_update(set2) - {set1}")  # Output - {1, 2, 5, 6}







