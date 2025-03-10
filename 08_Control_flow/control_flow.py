# Control flow.

# x = 7
# if x == 5:
#     print("x is 5")
# else:
#     print("x is not 5")

"""
if expression:
    execute statement(s)
elif expression:
    execute statement(s)
elif expression:
    execute statement(s)
else:
    execute statement(s)
"""

# x = 10
# print(f"x == 10 evaluates to - {x == 10}")
# print(f"x == 9 evaluates to - {x == 9}")

# some_flag = False
# if some_flag:  # some_flag == True
#     print(f"Code block starts here. Since some_flag evaluates to True, the code block executes.")
#     print(f"A code block is defined by a ':' at the end of a statement like")
#     print(f"if, elif, else statement. This indicates beginning of a block.")
#     print(f"All the code after the ':' is right indented (shifts right) by 4 spaces.")
#
#     print("Even if there is a space between two lines, code block continues")
#     print("This statement is the last line of the code block.")
#
# print(f"When indentation is removed, the block ends a line before.")

# if and else
# aFlag = False
# if aFlag:
#     print("Flag is set to True")
# else:
#     print("Flag is set to False")


# if, elif and else

# var = 9
# if var == 4:
#     print("Value of var is 4")
# elif var == 5:
#     print("Value of var is 5")
# elif var == 6:
#     print("Value of var is 6")
# else:
#     print("Value of var is not known")


# empty_string = 'test'
# empty_list = []
# empty_tuple = ()
# empty_set = set()
# empty_dict = {}
# num = 0
#
# if empty_string:
#     print("Object has data")
# else:
#     print("Object has no data")


# if - with multiple expressions.
# x = 5
# if x == 5 or x == 10:
#     print("X is either 5 or 10")
# else:
#     print("x is neither 5 nor 10")


# x = 5
# if x > 4 and x < 8:
#     print("X is between 4 and 8")
# else:
#     print("x is not between 4 and 8")


# x = 10
# if (x == 5 or x == 10) and x % 5 == 0:
#     print("X is either 5 or 10")
# else:
#     print("x is neither 5 nor 10")


# Using is operartor with if
# check variable type
# identity of two variables

"""
>>> x = 123456789
>>> y = x
>>> print(x is y)  # Outputs - True

>>> print(id(x), id(y)) # Outputs - 2436440817520 2436440817520

>>> z = 123456789
>>> print(x is z)  # Outputs - False

>>> print(id(x), id(z))  # Outputs - 2436440817520 2436440801904
"""

# x = 100
# if type(x) is int:
#     print("x is an integer variable")
# else:
#     print("x is not an integer variable.")

# if, elif and else statement - revision
"""
Control flow controls the flow of a program based on the conditions mentioned in a program.

Python provides conditional statements, loops, functions, and exceptions for control flow.

Elif (else if) and else statements are optional with an if statement.

Both if and elif evaluate an expression that uses a Boolean context.

If an expression evaluates to True, the corresponding code segment will execute.

When an if statement has elif and else statements, these conditions are mutually 
    exclusive. When one condition evaluates to True, the remaining conditions are not evaluated.

While working with objects of different data types (string, list, tuple, set, dictionary), when
    an object has no value or is empty, it is evaluated as False in the if expression.

In the case of an integer, the variable evaluates to False when its value is 0. Otherwise, it
    evaluates to true.

You can evaluate multiple expressions using an and/or operator. 

When "and" is used, expressions on either side of the operator must evaluate to True for the
    overall expression to be True.

When "or" is used, then any one expression on either side of the operator when evaluates 
    to True the overall expression is evaluated to True.
    
When evaluating multiple expressions, the evaluation sequence is from left to right.

When you use "is" with the if statement, then use it to check the datatype of a variable or
    to check the identity of two variables. 

Do not use "is" to compare the value of two variables. 

"""

# Match-case statement.

# match = 10
# case = 20
# print(match, case)
#
# def match():
#     pass


# import random
#
# x = random.randint(1, 7)
# match x:
#     case 1:  # think of this as if statement
#         print("one")
#     case 2:  # think of this as elif statement
#         print("two")
#     case 3:  # think of this as elif statement
#         print("three")
#     case 4:  # think of this as elif statement
#         print("four")
#     case _:  # think of this as an else statement
#         print("unknown number")


# while loop

"""
while(condition == True):
    execute statement(s)
    if some_break_condition == True:
        break (breaks from the loop)
else:
    execute statement(s) 
    These execute when the while loop terminates as its condition becomes False. 
    These do not execute when loop terminates using break statement.
"""

# x = 0
# while x < 5:
#     print(x, end=" ")
#     x += 1
# else:
#     print("\nWhile loop executes successfully.")


# x = 0
# while x < 5:
#     print(x, end=" ")
#     x += 1
#     if x == 3:
#         break
# else:
#     print("\nWhile loop executes successfully.")


# while loop with continue statement


# x = 0
# while x < 5:
#     x += 1
#     if x == 3:
#         continue
#     print(x, end=" ")
# else:
#     print("\nWhile loop executes successfully.")


# for loop

"""
for variable in sequence:
    execute statement(s)
    if some_break_condition == True:
        break (breaks from the loop)
else:
    execute statement(s) 
    These execute when the for loop completes its iterations. 
    These do not execute when loop terminates using break statement.
"""

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number, end=" ")
# else:
#     print("\nFor loop executes successfully")


# for number in range(5):
#     if number == 3:
#         break
#     print(number, end=" ")
# else:
#     print("\nFor loop executes successfully")


# for number in range(5):
#     if number == 3:
#         continue
#     print(number, end=" ")
# else:
#     print("\nFor loop executes successfully")


# range()
"""
range(start, stop, step)
Generally, with for loops, which run certain number of times, the function range()
comes very handy. This function return an object that produces a sequence of integers 
from start (inclusive) to stop (exclusive) by step.

start - is the starting number with which the list will start. Default is 0.  
stop - is the number at which the list ends. This is Required. 
    Note: the list will start 1 number before the *stop*.  
step - This mentions a gap between the 2 numbers in a list. Default is 1. 
"""

my_list = list(range(10))
print(my_list)
















