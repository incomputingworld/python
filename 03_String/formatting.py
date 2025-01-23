"""
This file contains various examples of modifers that you can use with f-string.

"""

# string formatting...
my_string = "abcd"
my_bg_str = "abcdefghijklmn"
fract = 0x00BC
jap_A = 0x3042
print("String formatting...")
print(f"String {my_string} left aligned within 10 spaces - |{my_string:<10}|")
print(f"String {my_string} right aligned within 10 spaces - |{my_string:>10}|")
print(f"String {my_string} center aligned within 10 spaces - |{my_string:^10}|")
print(f"String {my_string} 10 spaces fill with custom characters - |{my_string:*^10}|")
print(f"My_Bg_str {my_bg_str}) truncate. Show first 10 characters - {my_bg_str:.10}")
print(f"Vulgar fraction {fract} unicode value in character - {chr(fract)}")
print(f"Japanese A {jap_A} unicode value in charcter - {chr(jap_A)}")


# number formatting
big_num = 1234567890987654321
number = 1234
flt_num = 123.65284
progress = .83
bin_num = 0b10101011
print("Number formatting...")
print(f"Float {flt_num} with 3 decimal points - {flt_num:.3f}")
print(f"Number {number} in octal - {number:o}")
print(f"Number {number} in lowercase hexadecimal - {number:x}")
print(f"Number {number} in uppercase hexadecimal - {number:X}")
print(f"Number {number} in Binary - {number:b}")
print(f"Binary {bin_num:b} in decimal - {bin_num:d}")
print(f"Binary {bin_num:b} in hexadecimal - {bin_num:x}")
print(f"Number {flt_num} in Scientific notation - {number:e}")
print(f"BigNum {big_num} in Scientific notation - {big_num:e}")
print(f"Number {number} 10 space padding with Zero - |{number:010}|")
print(f"BigNum {big_num} comma as a thousand separator - {big_num:,}")
print(f"Combination {big_num} with padding and comma - {big_num:030,}")
print(f"Progress {progress} percentage formatting - {progress:.0%}")


