# keywords and operators
# help('keywords')

# Operators -
x = 10
# y = 10
# print(x + y)
"""
Arithmetic Operators - 
Operator    Meaning             Example
+	        Addition	        5 + 3 = 8
-	        Subtraction	        5 - 3 = 2
*	        Multiplication	    5 * 3 = 15
/	        Division (float)    5 / 2 = 2.5
//	        Division (Floor)	5 // 2 = 2
%	        Modulus (Remainder)	5 % 2 = 1
**	        Exponentiation	    5 ** 2 = 25

Comparison operator - 
Operator	Description	                Example
==	        Equal to	                5 == 3 → False
!=	        Not equal to	            5 != 3 → True
>	        Greater than	            5 > 3 → True
<	        Less than	                5 < 3 → False
>=	        Greater than or equal to	5 >= 5 → True
<=	        Less than or equal to	    5 <= 3 → False

Logical Operators - 
Operator	Description	                                        Example
and	        Returns True when both conditions are true	        True and False → False
or	        Returns True when at least one condition is true	True or False → True
not	        Reverses the result of a condition	                not True → False
"""
# x = 7
# # print((x > 5) and (x < 10))
# # print((x > 5) or (x < 2))
#
# print(not False)

"""
Assignment operator - 
Operator	Description	                Example
=	        Assigns value	            x = 5
+=	        Adds and assigns	        x += 3 → x = 8
-=	        Subtracts and assigns	    x -= 3 → x = 2
*=	        Multiplies and assigns	    x *= 3 → x = 15
/=	        Divides and assigns	        x /= 2 → x = 2.5
%=	        Modulus and assigns	        x %= 2 → x = 1
**=	        Exponent and assigns	    x **= 2 → x = 25
//=	        Floor divide and assigns	x //= 2 → x = 2

Membership operator - 
Operator	Description	                        Example
in	        Returns True if value is present	'a' in 'apple' → True
not in	    Returns True if value is absent	    'b' not in 'apple' → True

"""
# my_list = [1,2,3,4,5]
# print(5 in my_list)  # True
# print(7 in my_list)  # False
# print(9 not in my_list)  # True

"""
Identity Operator - 

Operator	Description	                                Example
is	        Returns True if objects are identical	    x is y
is not	    Returns True if objects are not identical	x is not y

"""
# a = 35274983
# b = 35274983
# print(a is b)
# print(id(a), id(b))

"""
Binary Operator - 

Operator	Description	                                            Example
&           AND - Sets to 1 when bits of both operands is 1         1100 & 1101 → 1100
|           OR - Sets to 1 when any one bit of both operands is 1   1100 | 1101 → 1101
^           XOR - Sets to 1 when one bit of both operands is 1      1100 | 1101 → 0001
~           NOT - Inverts the bits of an operand                    ~1100 → 0011
>>          Right Shift - Shifts bits of a number to the right by   1100 >> 2 → 0011
            specified number of times
<<          Left Shift - Shifts bits of a number to the left by     0011 << 2 → 1100
            specified number of times
AND
1100
1101
-----
1100

OR
1100
1101
-----
1101

XOR
1100
1101
-----
0001

"""
# x = 12
# print(f"{x} - {x:08b}")
# x = x >> 3
# print(f"{x} - {x:08b}")
# x = x << 3
# print(f"{x} - {x:08b}")

"""
Ternary Operator - 
Use this to put a conditional expression in short form on single line
It evaluates a condition and returns one of the two values based on a condition.

"""

result = 10 if 5 < 7 else 20
print(result)

















