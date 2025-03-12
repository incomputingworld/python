# Functions.

"""
A Function is a block of code which performs a specific task.
It can take an input, process the information, and return an output.
It is reusable; I can use this function in different parts of a program.
I use it to organize code, reduce repetition, and modularize code.
"""

# Function in Python

"""
def function_name(optional parameters):
    code block
    return "optional statemente"
"""

# def test():
#     print("Hey There")
#
#
# test()


# function return statement

# def test1():
#     print("Function with no return statement, return None")
#
# # print(test1())
#
#
# def test2():
#     print("Function with a return statement, returns None")
#     return
#
# # print(test2())
#
#
# def test3():
#     print("Function returning an expression")
#     return True # It can be any literal, variable or object
#
# # print(test3())
#
#
# def test4():
#     print("Function returning more than one value")
#     return 1, 2, 3, 4
#
# result = test4()
# print(type(result), result)


# arguments vs parameters

# def greet(name):
#     print(f"My name is {name}")
#
# greet("Sunil")


# Function parameters

# Required / Positional parameters
# def greet(name, age):
#     print(f"My name is {name} and I am {age} years old")
# greet("Abc", 25)
# greet("Abc")

# Default arguments

# def greet1(name, age=18):
#     print(f"My name is {name} and I am {age} years old")
#
# greet1("Abc", 25)
# greet1("Def")
#
# greet1(name='XYZ', age=15)
#
# greet1(age=10, name='ABC')
# greet(age=12, name="IJK")


# Named parameters

# def connect_to_db(server, port=20, *, usr, passwrd):
#     print(f'Connecting to {server} on {port} with user={usr} and password = {passwrd}')
#
#
# connect_to_db('localserver', usr='abc', passwrd='abc')
# connect_to_db('localserver', port=8080, usr='abc', passwrd='abc')
# # connect_to_db('localserver', 'abc', passwrd='abc')
#
# connect_to_db(port=8080, usr='abc', server='localserver', passwrd='abc')


# Position-only parameters

# def greet2(name, /, age):
#     print(f"My name is {name} and I am {age} years old.")
#
# greet2("Abc", 10)
# greet2(age=20, name="XYZ")


# variable length arguments - *args

# def add_numbers(*args):
#     print(args)
#     print(*args)
#     return sum(args)
#
# result = add_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(result)
#
#
# def test2(a, b, *args):
#     print(a, b, args)
#
# test2(10, 20, 30, 40, 50)


# variable length parameters - **kwargs


# def keys_values(**kwargs):
#     print(kwargs)
#     print(*kwargs)
#     for key, value in kwargs.items():
#         print(key, value)


# keys_values(name='Abc', age=25, hobby='cycling')


# def flexible_function(a, b, /, c, *, d, e, **kwargs):
#     print(f"Positional-Only: {a}, {b}")
#     print(f"Positional/Keyword: {c}")
#     # print(f"Variable length - *args: {args}")
#     print(f"Keyword-Only: {d}, {e}")
#     print(f"Variable length- **kwargs: {kwargs}")


# flexible_function(1, 2, c=3, d=7, e=8, f=9, g=10)


# Variable scoping

# def test():
#     x = 10
#     print(x)
#
# test()
# print(x) # error statement.

# x = 100
# print(locals())
# def test():
#     # x = 200
#     global x
#     x = 500
#     print(locals())
#     print(x)  # 500
#
# test()
# print(x)  # 500
#
#
# # globals()


# Enclosing scope

# def outer():
#     x = 20
#     print("outer locals -", locals())
#     def inner():
#         y = 30
#         nonlocal x
#         x = 50
#         print("inner locals -", locals())
#         print(x, y)
#
#     inner()
#     print(x)

# outer()


# w_global = 10  # global scope
# print("global", locals())  # namespace - variables in context of global namespace
#
# def outer(param="default value"):
#     x_nonlocal = 100  # enclosing scope
#     print("outer", locals())  # namespace - variables in context of outer function
#
#     def inner():  # nested function
#         y_local = 200  # local scope
#         global w_global  # use with globally defined variables
#         nonlocal x_nonlocal  # use with enclosed variables
#         x_nonlocal = 500
#         print("inner", locals())  # namespace - variables in context of inner function
#         print(w_global, x_nonlocal, y_local, param)  # 10 500 200 default value
#
#     inner()
#     print(w_global, x_nonlocal, param)  # 10 500 default value
#
# outer()


# Global scope
# x = 15
# print(x)


# Built-in scope

# print(dir(__builtins__))


# Pass by value and pass by reference

# Pass By value
# def test(value_param):
#     print("test - ", id(value_param), value_param)
#     value_param = 123452
#     print("test - ", id(value_param), value_param)
#
# x = 20
# print("Global - ", id(x), x)
# test(x)
# print("Global - ", id(x), x)

# Pass by Reference
def test(ref_param):
    print("test - ", id(ref_param), ref_param)
    # ref_param[0] = "test"
    ref_param = [11, 12, 13]
    print("test - ", id(ref_param), ref_param)

my_list = [1, 2, 3]
print("Global - ", id(my_list), my_list)
test(my_list)
print("Global - ", id(my_list), my_list)

















