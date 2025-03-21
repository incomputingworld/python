# Exception management.
""""""

# Exception handling.


# Python Exception Management.
"""
BaseException
  Exception
    ArithmeticError
      FloatingPointError
      OverflowError
      ZeroDivisionError
    AssertionError
    AttributeError
    EOFError
    ImportError
      ModuleNotFoundError
    IndexError
    KeyError
    MemoryError
    NameError
      UnboundLocalError
    OSError
      FileNotFoundError
      PermissionError
      TimeoutError
    ValueError
      UnicodeError
"""

# Handling an exception
"""
try:
    This contains a potentially problematic code block.
    Code that can cause an exception.
except (mention expected exceptions):
    Code block to execute when exception occurs
else:
    Optional code block to execute when exception does not occur
finally:
    Optional last Code block to execute whether exception occurs or not
"""


# def divideNums(x, y):
#     result = None
#     try:
#         result = x / y
#     except ZeroDivisionError as e:
#         print("Error - ", e)
#     else:
#         print("Else - Division is successful")
#     finally:
#         print("Finally - Division is Complete")
#     return result
#
#
# print(divideNums(10, 0))


# 1. When an exception is not handled, the program terminates abruptly.
# Throws the stack on the std error.
def no_exception_handling():
    print(xval)


# no_exception_handling()



# 2. Handling exception in generic way. Not a good practice. Avoid this.
import sys

def generic_exception_handler():
    try:
        print(5 / 0)
    except:
        print(str(sys.exc_info()))  # information about current exception

# generic_exception_handler()


# 3. A good example of exception handling. Using a specific exception.
def specific_exception_handler():
    try:
        print(xval)
    except NameError as e:  # Handling specific NameError.
        print(str(e))
        print("You can use this to log or show a user-friendly message"
              "and possibly do a graceful termination of application")
        print("Compare this against the first function, no_exception_handling()")

# specific_exception_handler()



# 4. Function handling multiple exceptions
def divide_multiple_exceptions(x, y):
    result = None
    try:
        result = x / y
    except (ZeroDivisionError, TypeError) as e:  # You can mention multiple exceptions in a tuple
        print(e)
        print(f"When a function does specific exception handling, it means")
        print(f"a programmer has done a due diligence in writing code.")
        print("When function has an unhandled exception, it means programmer")
        print("has not updated the exception handling code accordingly.")
    return result


# divide_multiple_exceptions(5, 0)
# divide_multiple_exceptions(5, "2")



# 5. Function handling specific exception and all other exceptions as well
def handle_all_exceptions(x, y):
    result = 0
    try:
        result = x / y

    except (ZeroDivisionError,) as e:  # tuple with one must have a comma (,) in the end
        print(e)

    except Exception as e:  # another style to handle single exception.
        print(e)
        print("When a function catches an exception it is not meant to handle or cannot handle")
        print("in that case the function must pass the exception back to the caller.")
        print("It should not consume it. Or change the function code to manage the exception")
    return result


# handle_all_exceptions(5, 0)
# handle_all_exceptions(5, "0")



# 6. Passing exception back to the caller. Re-raising an exception
def divide(x, y):
    try:
        return x / y
    except (ZeroDivisionError,) as e:
        print(e)
    except Exception as e:
        print("Since I do not know how to handle this exception, passing it back to the caller.")
        raise e
        # raise  # both the statements are correct

def test_divide():
    try:
        result = divide(5, "5")
        print(result)
    except TypeError as e:
        print("Exception caught by the calling function.")
        print(e)

# test_divide()

def test_divide1():
    print("No exception handling. This will cause abrupt program termination.")
    divide(5, "5")

# test_divide1()


# 7. Exception with else and finally block
def with_else_and_finally(x, y):
    result = None
    try:
        result = x / y
    except ZeroDivisionError as e:  # You can mention multiple exceptions in a tuple
        print("Zero division - ", e)
    except TypeError as e:
        print("Type Error - ", e)
    else:
        print("Else - executes when there is no exception.")
    finally:
        print("Finally - executes whether exception occurs or not.")
    return result


# print(with_else_and_finally(5, 2))  # Both else and finally execute here
# print(with_else_and_finally(5, 0))  # Only finally executes here


# 8. When the try block has a return statement
def try_with_return_statement(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    else:
        print("Else - will not execute because of return statement in try block.")
    finally:
        print("Finally - executes whether exception occurs or not.")

# print(try_with_return_statement(5, 2))  # else part does not execute. Finally executes



# 9. When both try and finally block has a return statement
def try_and_finally_with_return_statement(x, y):
    try:
        return x / y
    except (ZeroDivisionError, TypeError) as e:
        print(e)
    else:
        print("Else - executes when there is no exception.")
    finally:
        print("Finally - executes whether exception occurs or not.")
        return 100

# Finally executes. Else does not. Prints 100
# print(try_and_finally_with_return_statement(5, 2))
# print(try_and_finally_with_return_statement(5, "2"))




# 10. Raising an exception explicitly.
def is_positive(number):
    if number < 0:
        raise ValueError(f"The number must be positive!")  # raise a built-in exception
    return f"{number} is a positive number."


# Test the function
def check_positive(num):
    try:
        print(is_positive(num))  # This will raise a ValueError
    except ValueError as e:
        print(f"Exception caught: {e}")


# check_positive(10)
# check_positive(-10)



# 11. Example of raising a Runtime Exception
def raise_runtime_error():
    raise RuntimeError("Raised a runtime error.")

def manage_exception():
    try:
        raise_runtime_error()
    except RuntimeError as e:
        print(e)

# manage_exception()



# User defined exception

class CustomException(Exception):
    def __init__(self, msg, **kwargs):
        super().__init__(msg)  # Initialize base class
        self.msg = msg
        self.kwargs = kwargs

    def __str__(self):
        values = []
        for value in self.kwargs.values():
            values.append(value)
        return f"{self.msg} - with values - {values}"

def raise_custom_exception(message):
    raise CustomException(message, param1="Param1_Value", param2="Param2_Value")

def manage_custom_exception():
    try:
        raise_custom_exception("This is the exception message...")
    except CustomException as e:
        print(e)


manage_custom_exception()

















