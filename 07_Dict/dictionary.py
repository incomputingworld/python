# Dictionary. {}, dict()
"""

"""
# my_dict = {'name': "Abc"}
# print(my_dict)
# my_dict = {}
# my_dict1 = {"name": "ABC", "age": 25}
# print(my_dict1["age"])


# Characteristics
# Ordered.
# Mutable
# Unique and immutable Keys.
# Values are mutable
# Supports nesting
# person = {"name": "Abc", "age": 25,
#           "address": {"city": "Pune",
#                       "state": "Maharashtra"}}


# Add remove methods
"""
The easiest way to add a new key: value pair is by referring a new key name within square 
brackets and assign a value to it.
"""
# person = {"name": "Abc"}
#
# person["age"] = 25
# print(person)


# Add remove methods
"""
update(elements) - update method updates the dictionary with the new elements (key: value) pair
which can be another dictionary or an iterable
"""
# person = {"name": "Abc"}
# person.update({"age": 25})
# person.update(hobby='Cycling', exp=10)
# print(person)




# Add remove methods
"""
setdefault(key, default) - This method returns a value of the key. If the key does not exist
It inserts the key sets its value with default.
"""
# person = {"name": "Abc"}
# print(person.setdefault("name", "test"))  # Outputs - Abc
# print(person.setdefault("hobby", "cycling"))  # Outputs - cycling
# print(person.setdefault("age", 25))  # Outputs - 25
# print(person.setdefault("exp"))  # Outputs - None
# print(person)




# Add remove methods
"""
pop(key, default) - This function removes the "key: value" pair from a dictionary and returns
the value. 
If the key does not exist in the dictionary, it returns the default value.
And if the default value too is not defined then the function raises KeyError exception.
"""
# person = {"name": "Abc", "age": 25, "hobby": "Cycling"}
# print(person)  # Outputs - {'name': 'Abc', 'age': 25, 'hobby': 'Cycling'}
# print(f"Popped hobby, value is - {person.pop("hobby")}")  # Outputs - Cycling
# print(person)  # Outputs - {'name': 'Abc', 'age': 25}
# print(f"Popped invalid key with default value - "
#       f"{person.pop('RandomKey', 'No key found')}")  # Outputs - No key found
# print(f"Popped invalid key with no default value - "
#       f"{person.pop('RandomKey')}")  # Outputs - KeyError exception








# Add remove methods
"""
popitem() - This method returns the last "key: value" pair added in the dictionary.
It returns this in a tuple.
if the dictionary is empty, this function raises KeyError exception.

clear() - removes all the elements from a dictionary
"""

# person = {"name": "Abc", "age": 25, "hobby": "Cycling"}
# print(person)  # Outputs - {'name': 'Abc', 'age': 25, 'hobby': 'Cycling'}
# print(f"Popitem() - {person.popitem()}")  # Outputs - ('hobby', 'Cycling')
# print(person)  # Outputs - {'name': 'Abc', 'age': 25}
#
# person.clear()
# print(person)  # Outputs - {}
# # person.popitem()  # throws Exception - KeyError




# Accessing Values
"""
get(key, default) - This method returns the value of the key. 
If the key does not exist it returns the default value. 
If the default value is not mentioned either, then this function returns None. 
It does not remove the kay:value pair from the dictionary.
"""
# person = {"name": "Abc", "age": 25, "hobby": "Cycling"}
# print(f"Get key 'name' - {person.get('name')}")  # Outputs - Abc
# print(f"Invalid key, default value - "
#       f"{person.get('address', 'No key found')}")  # Outputs - No key found
# print(f"Invalid key, no default value - "
#       f"{person.get('address')}")  # Outputs - None
# print(person)  # Outputs - {'name': 'Abc', 'age': 25, 'hobby': 'Cycling'}




# Accessing Values
"""
keys() - This method returns a "view" object of the keys of a dictionary. It is of type 
dict_keys. 
This is a dynamic view, means, it reflects the changes made to the dictionary. 
A kind of live reference to dictionary keys. 
The keys appear to be like a list, but it is not a list. 
I cannot access an element using an index. 
But it is possible to loop through this view object.
Can do a membership checkon this view object.
"""
# person = {"name": "Abc", "age": 25, "hobby": "Cycling"}
# keysObj = person.keys()
# print(type(keysObj))  # Outputs - <class 'dict_keys'>
# print(keysObj)  # Outputs - dict_keys(['name', 'age', 'hobby'])
# person['address'] = 'India'
# print(keysObj)  # Outputs - dict_keys(['name', 'age', 'hobby', 'address'])
# # print(keysObj[0])  # Outputs - KeyError - 'dict_keys' object is not subscriptable
# print(f'name in keysObjs is -  {"name" in keysObj}')  # Outputs - True



# Accessing Values
"""
values() - This method returns a "view" object of the values of a dictionary. 
It is of type dict_values. 
This is a dynamic view, means, it reflects the changes made to the dictionary. 
A kind of live reference to dictionary values. 
The values appear to be like a list, but it is not a list. 
I cannot access an element using an index. 
But it is possible to loop through this view object and do a membership check 
"""
# person = {"name": "Abc", "age": 25, "hobby": "Cycling"}
# valuesObj = person.values()
# print(type(valuesObj))  # Outputs - <class 'dict_values'>
# print(valuesObj)  # Outputs - dict_values(['Abc', 25, 'Cycling'])
# person['address'] = 'India'
# print(valuesObj)  # Outputs - dict_values(['Abc', 25, 'Cycling', 'India'])
# print(f'Abc in valuesObj is -  {"Abc" in valuesObj}')  # Outputs - True


# Accessing Values
"""
items() - This method is a combination of keys and values method.
It returns view object of both key: value pair, of a dictionary. It is of type dict_items. 
This is a dynamic view, means, it reflects the changes made to the dictionary. 
A kind of live reference to a dictionary.
Each element of this object is a tuple. This tuple contains both the key and its value.
This object too appears like a list, but it is not a list. 
I cannot access an element using an index. 
But it is possible to loop through this view object
"""
# person = {"name": "Abc", "age": 25}
# itemsObj = person.items()
# print(type(itemsObj))  # Outputs - <class 'dict_items'>
# print(itemsObj)  # Outputs - dict_items([('name', 'Abc'), ('age', 25)])
# person['address'] = 'India'
# print(itemsObj)  # Outputs - dict_items([('name', 'Abc'), ('age', 25), ('address', 'India')])
# print(f"('name', 'Abc') in valuesObj is -  {('name', 'Abc') in itemsObj}")  # Outputs - True





# Membership check on dictionary
"""
When you want to do a membership check on a dictionary, then you do this on the "keys" of
a dictionary.
"""
person = {"name": "Abc", "age": 25, "hobby": "Cycling"}
print(f"Checking key 'name' in person - {'name' in person}")  # Outputs - True
print(f"Checking key 'Job' not in person - {'Job' not in person}")  # Outputs - True













