# Classes.
""""""
# Defining a class

# class Calculator:
#     def __init__(self, xVal, yVal):
#         self.x = xVal  # attribute
#         self.y = yVal  # attribute
#
#     def add(self):  # method
#         return self.x + self.y
#
#     def subtract(self):  # method
#         return self.x - self.y
#
#     def multiply(self):  # method
#         return self.x * self.y
#
#     def divide(self):  # method
#         return self.x / self.y
#
# calcObj = Calculator(10, 2)
# print(calcObj.add())


# Dunder or magic method
# class Calculator:
#     def __init__(self, xVal, yVal):
#         self.x = xVal  # attribute
#         self.y = yVal  # attribute
#
#     def add(self):  # method
#         return self.x + self.y
#
#     def subtract(self):  # method
#         return self.x - self.y
#
#     def multiply(self):  # method
#         return self.x * self.y
#
#     def divide(self):  # method
#         return self.x / self.y
#
#     def __str__(self):
#         return f"Calculator - x = {self.x}; y = {self.y}"
#
# calcObj = Calculator(100, 5)
# print(calcObj)

# Access specifiers
"""
Help in defining the scope of accessibility of methods and attributes of a class.

Languages like C++ or Java which provides private, protected and public keywords to define 
the access scope of class attributes/methods. This means…

Private - class attributes/methods are not accessible outside the class. 
Only the class methods can access these attributes. 
These members are not available to a subclass

Protected - class attributes/methods are not accessible outside the class. 
Only the class methods can access these attributes. 
These members are available to a subclasses

Public - class member (mostly the methods) are accessible outside the class. 
Objects operate on these methods.
These members are available to a subclasses
"""
# This class is written to show how C++/Java uses access specifiers.
# class Test:
#     def __init__(self):
#         self.public_attribute = 0
#
#     def public_method(self):
#         print("This is a private method. It has access to private attributes")
#         print(self.public_attribute)  # Valid statement
#
#
#
# test = Test()
# #  below two statements are valid
# test.public_attribute
# test.public_method()


# class Test:
#     def __init__(self):
#         self.public_attr = 10
#         self._protected_attr = 20
#         self.__private_attr = 30
#
#     def public_method(self):
#         print("Public method - ", self.public_attr, self._protected_attr, self.__private_attr)
#
#     def _protected_method(self):
#         print("Protected method - ", self.public_attr, self._protected_attr, self.__private_attr)
#
#     def __private_method(self):
#         print("Private method - ", self.public_attr, self._protected_attr, self.__private_attr)
#
# test = Test()
# # test.public_method()
# # test._protected_method()
# # print(test.public_attr, test._protected_attr)
# # test.__private_method()
#
# test._Test__private_method()
# print(test._Test__private_attr)

# Getters and Setters


# class TestClass:
#     def __init__(self, val):
#         self._value = val  # recommended as protected
#
#     @property  # decorator
#     def value(self):
#         print("getter", end=" ")
#         return self._value
#
#     @value.setter  # decorator
#     def value(self, new_val):
#         if new_val > 50:
#             print("setter - attribute updated")
#             self._value = new_val
#
# test = TestClass(55)
# # print(test.value)
# # test.value = 30
# # print(test.value)
# # test.value = 300
# # print(test.value)
# print(test._value)
#


# Knowing self...

class User:
    def __init__(self, nameVal, ageVal):
        self.name = nameVal
        self.age = ageVal

    def get_name(self):
        return self.name

    def set_name(self, newName):
        newName.strip()
        if newName:
            self.name = newName


amit = User("Amit", 25)
kapil = User("Kapil", 20)

print(kapil.get_name())
print(User.get_name(kapil))















