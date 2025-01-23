# Strings.

# my_str = "test"
# my_str = 'test'
# # my_str = 'test" # error
# my_str ="dad's car"
# my_str = 'This is a "great" deal'
# my_str = 'dad\'s car'

# my_str = """First line
# Second line
#       third with spaces """
# print(my_str)

name = "Abc"
age = 25
strn = f"My name is {name}. I am {age} years old. After 5 years I will be {age + 5}"
# print(strn)

num = 12
odd_even = f"The number {num} is {'even' if num % 2 == 0 else 'odd'}"
# print(odd_even)

mod_strn = f" Num in Hexadecimal - {num:x}, binary - {num:b}, float - {num:.2f}"
# print(mod_strn)

# mod_strn = f"Formatted String/ Left aligned {name:<15}, right aligned {name:>15}."
# print(mod_strn)


# Traversal and slicing




"""
string[start: end: step]
start - starting index
end - ending index (exclusive)
step - 1
"""
# Read complete string
# my_string = "In Computing World"
# print(f"my_string[:] - {my_string[:]}")
# print(f"my_string[0:] - {my_string[0:]}")
# print(f"my_string[:18] - {my_string[:18]}")
# print(f"my_string[:20] - {my_string[:20]}")  # throws no error

# my_string = "In Computing World"
# print(f"my_string[3:12] - {my_string[3:12]}")  # prints Computing
# print(f"my_string[3:12:2] - {my_string[3:12:2]}")  # prints Cmuig
# print(f"my_string[3:12:3] - {my_string[3:12:3]}")  # prints Cpi
# print(f"my_string[4:4] - {my_string[4:4]}")  # prints empty string
# print(f"my_string[20:4] - {my_string[20:4]}")  # prints empty string
# print(f"my_string[5:4] - {my_string[5:4]}")  # prints empty string



# my_string = "In Computing World"
# print(f"my_string[-1:] - {my_string[-1:]}")  # prints d
# print(f"my_string[-18:] - {my_string[-18:]}")  # prints In Computing World
# print(f"my_string[-18:-1:] - {my_string[-18:-1]}")  # prints In Computing Worl
# print(f"my_string[:-18]) - {my_string[:-18]}")  # prints empty string
# print(f"my_string[-15:-6] - {my_string[-15:-6]}")  # prints Computing
# print(f"my_string[-1: -10] - {my_string[-1: -10]}")  # prints empty string
# my_String[17:] -  -1+18 = 17
# -18 + 18 = 0 my_string[0:]
# my_string[0:17]
# my_string[0:0]
# my_string[3:12]
# my_string[17:8]


# my_string = "In Computing World"
# print(f"my_string[-15:-6: 2] - {my_string[-15:-6: 2]}")  # prints Cumig
# print(f"my_string[-15:-6: -2] - {my_string[-15:-6: -2]}")  # prints empty string
# print(f"my_string[-6:-15: -2] - {my_string[-6:-15: -2]}")  # prints  ntpo
#
#
# print(f"my_string[11:2:-1] - {my_string[11:2:-1]}")  # prints gnitupmoC
# print(f"my_string[::-1] - {my_string[::-1]}")  # prints dlroW gnitupmoC nI
# my_String[3: 12: 2] - Cumig
# my_String[3: 12: -2] -
# my_String[12: 3: -2] - ntpo
# my_String[11: 3: -1]
# my_String[0: 18: -1]

"""
Search and find

find(sub, start, end): Returns the index of the first occurrence of a substring.
index(sub, start, end): Like find(), but raises a ValueError if not found.

rfind(sub, start, end): Returns the index of the last occurrence of a substring.
rindex(sub, start, end): Like rfind(), but raises a ValueError if not found.

count(sub, start, end): Counts the occurrences of a substring.


"""
# my_string = "IN COMPUTING WORLD"
# print(f"my_string.find('IN') - {my_string.find('IN')}")  # prints 0
# print(f'my_string.find("in") - {my_string.find("in")}')  # prints -1
# print(f'my_string.find("IN", 5) - {my_string.find("IN", 5)}')  # prints 9
# print(f'my_string.find("IN", 0, 2) - {my_string.find("IN", 0, 2)}')  # prints 0
#
# print(f'my_string.index("IN") - {my_string.index("IN")}')  # prints 0
# print(f'my_string.index("IN", 0, 2) - {my_string.index("IN", 0, 2)}')  # prints 0

# Below statements - # throws ValueError: substring not found
# print(f'my_string.index("CO", 5) - {my_string.index("CO", 5)}')
# print(f'my_string.index("in") - {my_string.index("in")}')

# my_string = "IN COMPUTING WORLD"
# print(f"my_string.rfind('IN') - {my_string.rfind('IN')}")  # prints 9
# print(f'my_string.rfind("in") - {my_string.rfind("in")}')  # prints -1
# print(f'my_string.rfind("IN", 5) - {my_string.rfind("IN", 5)}')  # prints 9
# print(f'my_string.rfind("IN", 0, 2) - {my_string.rfind("IN", 0, 2)}')  # prints 0
#
# print(f'my_string.rindex("IN") - {my_string.rindex("IN")}')  # prints 9
# print(f'my_string.rindex("IN", 0, 2) - {my_string.rindex("IN", 0, 2)}')  # prints 0
#
# # Below statements - # throws ValueError: substring not found
# # print(f'my_string.rindex("in") - {my_string.rindex("in")}')
# # print(f'my_string.rindex("CO", 5) - {my_string.rindex("CO", 5)}')
#
# print(f'my_string.count("IN") - {my_string.count("IN")}')  # prints 2
# print(f'my_string.count("IN") - {my_string.count("i")}')  # prints 0


# Replace and Substitute.
"""
replace(old, new, count): Replaces occurrences of a substring with another.
old - substring we want to replace
new - substring we want to replace old with
count - number of times we want to do this replacement. By default, all occurances of "old"
is replaced by "new".
"""

# my_string = "One two One or One to Many. So many, yet count starts from one."
# updated_string = my_string.replace("One", "1")
# print(updated_string)
# updated_string = my_string.replace("One", "1", 1)
# print(updated_string)
# updated_string = my_string.replace("00ne", "1", 1)


# Split and join
"""

split(sep, maxsplit) - Splits the string at a separator
rsplit(sep, maxsplit) - Splits the string from the right

  sep (optional) - Specifies the delimiter used to split the string.   
  If not provided, whitespace is used as the default delimiter.
  maxsplit (optional) - Determines the maximum number of splits. 
  If not provided, the default value is -1, which means there is no limit 
  on the number of splits.

"""

# alphabets = "A. B. C. D. E"
# print(f'alphabets.split() - {alphabets.split()}')
# print(f'alphabets.split(".") - {alphabets.split(".")}')
# print(f'alphabets.split(". ") - {alphabets.split(". ")}')
# print(f'alphabets.split(".  ") - {alphabets.split(".  ")}')
#
# print(f'alphabets.split(". ", 2) - {alphabets.split(". ", 2)}')
# print(f'alphabets.rsplit(". ", 2) - {alphabets.rsplit(". ", 2)}')

# Split and join...
"""
partition(sep): Splits a string in two parts at first occurance of specified delimiter.
Returns a tuple with 3 elements. 
  1. Part of the string before a separator
  2. the seprarator
  3. Part of the string after the separatorrr
rpartition(sep): Similar to partition() but starts from the right.
  sep - Specifies the delimiter used to split the string.

"""

# alphabets = "A. B. C. D. E"
# part_strn = alphabets.partition(". ")
# print(f'alphabets.partition(". ") - {part_strn}')
#
# part_strn = alphabets.rpartition(". ")
# print(f'alphabets.rpartition(". ") - {part_strn}')
#
# part_strn = alphabets.partition(".  ")
# print(f'alphabets.partition(".  ") - {part_strn}')
#
# full_path = "C:\\test\\myfile.txt"
# print(full_path.rpartition("\\"))


# Split and join...
"""
splitlines(keepends=False): Splits the string at line breaks. The line break characters
    are (\n) - newline character or (\r) - carriage return.
    keepends(optional) - When set to True line break character is included in the 
    resulting list. Default value is False 
"""
# ml_string = "Hello!!\nHow are you?\rBeen a long time.\nWhere are you now-a-days?"
# ml_list = ml_string.splitlines()
# print(ml_list)
#
# ml_list = ml_string.splitlines(True)
# print(ml_list)


# Split and join...
"""
join(iterable)
  accepts an iterable (an object that can return its elements one at a time) and 
  returns a string after joining the elements by the given string separator.
"""

# my_list = ['In', 'Computing', 'World']
#
# # empty string as a separator; prints - InComputingWorld
# separator = ''
# print(f"separator.join(my_list) - {separator.join(my_list)}")
# print(f"''.join(my_list) - {''.join(my_list)}")
#
# # space character is the separator; prints - In Computing World
# separator = ' '
# print(f"separator.join(my_list) - {separator.join(my_list)}")
# print(f"' '.join(my_list) - {' '.join(my_list)}")
#
# # comma as a separator; prints - In,Computing,World
# separator = ','
# print(f"separator.join(my_list) - {separator.join(my_list)}")
# print(f"','.join(my_list) - {','.join(my_list)}")


# Character type checks...
"""
islower() - Checks if all characters are lowercase and returns True. Otherwise False.
    It ignores white spaces, numbers, special characters

isupper() - Checks if all characters are uppercase and returns True. Otherwise False.
    It ignores white spaces, numbers, special characters

isspace(): Checks if all characters are whitespace and returns True. Otherwise False.

"""
# print(f"'abcd '.islower() - {'abcd '.islower()}")
# print(f"'abcd ½123'.islower() - {'abcd ½123'.islower()}")
# print(f"'  abcd 123'.islower() - {'  abcd 123'.islower()}")
# print(f"'123abcd 123'.islower() - {'123abcd 123'.islower()}")
# print(f"'123Abcd 123'.islower() - {'123Abcd 123'.islower()}")

# print(f"'ABC'.isupper() - {'ABC '.isupper()}")
# print(f"'ABC 123'.isupper() - {'ABC 123'.isupper()}")
# print(f"'  ABC 123'.isupper() - {'  ABC 123'.isupper()}")
# print(f"'123ABC 123'.isupper() - {'123ABC 123'.isupper()}")
# print(f"'123aBC 123'.isupper() - {'123aBC 123'.isupper()}")


# print(" ".isspace())
# print("".isspace())
# print(" a".isspace())

# Character type checks...
"""
isalpha(): When all characters are alphabets (lower/upper) returns True.
    White spaces, numbers, special characters cause this function to return False
     
isalnum(): When all characters are alphabets (lower/upper) or digits (0-9) returns True.
    White spaces, special characters cause this function to return False
"""

# print(f"'AbCdE'.isalpha() - {'AbCdE'.isalpha()}")
# print(f"'AbCdE '.isalpha() - {'AbCdE '.isalpha()}")
# print(f"'AbCdE 123'.isalpha() - {'AbCdE 123'.isalpha()}")
#
# print(f"'aB145'.isalnum() - {'aB145'.isalnum()}")
# print(f"'aB145 '.isalnum() - {'aB145 '.isalnum()}")










# Character type checks...
"""
isdecimal() - returns True when the number is a decimal digit of base 10. 

isdigit() - returns True when the given string has a number in it. 
    This includes numbers mentioned in superscript, subscript, or circled digit.

isnumeric() - return True when the given string contains numbers, fractions, 
    digits, subscripts, superscript, etc

"""

# Decimal Number - '12345'
# print(f"'12345'.isdigit() - {'12345'.isdigit()}")
# print(f"'12345'.isdecimal() - {'12345'.isdecimal()}")
# print(f"'12345'.isnumeric() - {'12345'.isnumeric()}")
#
# # Decimal Number with space - '12345 '
# print(f"'12345 '.isdigit() - {'12345 '.isdigit()}")
# print(f"'12345 '.isdecimal() - {'12345 '.isdecimal()}")
# print(f"'12345 '.isnumeric() - {'12345 '.isnumeric()}")
#
# # Vulgar faction - ¼
# print(f"'¼'.isdigit() - {'¼'.isdigit()}")
# print(f"'¼'.isdecimal() - {'¼'.isdecimal()}")
# print(f"'¼'.isnumeric() - {'¼'.isnumeric()}")
#
# # Arabic 9
# print(f"'۹'.isdigit() - {'۹'.isdigit()}")
# print(f"'۹'.isdecimal() - {'۹'.isdecimal()}")
# print(f"'۹'.isnumeric() - {'۹'.isnumeric()}")
#
# #  Hindi - (1) १
# print(f"'१'.isdigit() - {'१'.isdigit()}")
# print(f"'१'.isdecimal() - {'१'.isdecimal()}")
# print(f"'१'.isnumeric() - {'१'.isnumeric()}")
#
# #  Circled numbers - ⑩
# print(f"'⑩'.isdigit() - {'⑩'.isdigit()}")
# print(f"'⑩'.isdecimal() - {'⑩'.isdecimal()}")
# print(f"'⑩'.isnumeric() - {'⑩'.isnumeric()}")
#
# # Superscript Number - ⁵
# print(f"'⁵'.isdigit() - {'⁵'.isdigit()}")
# print(f"'⁵'.isdecimal() - {'⁵'.isdecimal()}")
# print(f"'⁵'.isnumeric() - {'⁵'.isnumeric()}")
#
# #  Circled digit - ⓪
# print(f"'⓪'.isdigit() - {'⓪'.isdigit()}")
# print(f"'⓪'.isdecimal() - {'⓪'.isdecimal()}")
# print(f"'⓪'.isnumeric() - {'⓪'.isnumeric()}")
#
# # Power - '2⁷'
# print(f"'2⁷'.isdigit() - {'2⁷'.isdigit()}")
# print(f"'2⁷'.isdecimal() - {'2⁷'.isdecimal()}")
# print(f"'2⁷'.isnumeric() - {'2⁷'.isnumeric()}")

# String modifiction....
"""
upper() - convers all charcters to upper case
lower() - convers all charcters to lower case
capitalize() - capitalizes first character
title() - converts string to title case.
ljust(width, fillchar*): Left-aligns the string, padding with a character.
rjust(width, fillchar*): Right-aligns the string, padding with a character.
center(width, fillchar*): Centers the string, padding with a character.
fillchar* - is optional and default padding character is " " space.
"""
# my_string = 'in commputing world'
# print(f"'abc'.upper() - {'abc'.upper()}")
# print(f"'ABC'.lower() - {'ABC'.lower()}")
# print(f"my_string.capitalize() - {my_string.capitalize()}")
# print(f"my_string.title() - {my_string.title()}")
# print(f"'abcd'.ljust(10, ' ') - |{'abcd'.ljust(10)}|")
# print(f"'abcd'.rjust(10, ' ') - |{'abcd'.rjust(10, '@')}|")
# print(f"'abcd'.center(10, ' ') - |{'abcd'.center(10, '@')}|")


# Trim and strip....
"""
strip(chars): Removes leading and trailing characters.
lstrip(chars): Removes leading characters.
rstrip(chars): Removes trailing characters.

chars - when not specified, removes the white spaces. When specified, removes the 
characters until a mismatch occurs.

"""

# print("strip()")
# print(f'" abc de ".strip() -|{" abc de ".strip()}|')
# print(f'" abc de ".strip(" de ") - |{" abc de ".strip("de ")}|')
# print(f'"aebec de".strip("e") - |{"aebec de".strip("e")}|')
# print(f'"ab ab xyz ab ".strip("ab ") - |{"ab ab xyz ab ".strip("ab")}|')


# print("lstrip()")
# print(f'" abc de ".lstrip() -|{" abc de ".lstrip()}|')
# print(f'" abc de ".lstrip(" de ") - |{" abc de ".lstrip(" de ")}|')
# print(f'"aebec de".lstrip("e") - |{"aebec de".lstrip("e")}|')
# print(f'"ab ab xyz ab ".lstrip("ab ") - |{"ab ab xyz ab ".lstrip("ab ")}|')


# print("rstrip()")
# print(f'" abc de ".rstrip() -|{" abc de ".rstrip()}|')
# print(f'" abc de ".rstrip(" de ") - |{" abc de ".rstrip(" de ")}|')
# print(f'"aebec de".rstrip("e") - |{"aebec de".rstrip("e")}|')
# print(f'"ab ab xyz ab ".rstrip("ab ") - |{"ab ab xyz ab ".rstrip("ab ")}|')


# checking start/end with...
"""
startswith(prefix, start, end): Checks if the string starts with a prefix.
endswith(suffix, start, end): Checks if the string ends with a suffix.
"""

# my_string = "In Computing World"
# strs_to_look = ("On", "An", "In", "ld")
# print(f'my_string.startswith("In") - {my_string.startswith("In")}')
# print(f'my_string.startswith("in") - {my_string.startswith("in", 9)}')
# print(f'my_string.startswith(strs_to_look) - {my_string.startswith(strs_to_look)}')


# my_string = "In Computing World"
# strs_to_look = ("On", "An", "In", "ld")
# print(f'my_string.endswith("In") - {my_string.endswith("ld")}')
# print(f'my_string.endswith("in") - {my_string.endswith("in", 9, 11)}')
# print(f'my_string.endswith(strs_to_look) - {my_string.endswith(strs_to_look)}')

# UNICODE -

"""
encode(encoding='utf-8', errors='strict') - 
    This method is used to convert a string into a bytes object. 
    Encodes the string using a specified encoding scheme
decode(encoding='utf-8', errors='strict') - 
    This method is used to convert a bytes object back into a string. 
    Decoding the bytes using a specified encoding scheme.

Other errors options are
    backslashreplace - shows the Unicode value
    ignore - ignore invalid characters
    namereplace - shows the name of the character in the Unicdoe table
    replace - replace an invalid character with a placeholder.

"""
# my_string = "Japanese characters - あば"
# print(my_string)
# my_str_bytes = my_string.encode("utf-8")
# print(my_str_bytes)
# my_str = my_str_bytes.decode("utf-8")
# print(my_str)


txt = "Sũnil"
print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))














