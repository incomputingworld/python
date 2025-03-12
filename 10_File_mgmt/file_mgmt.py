# File management
""""""

# File open operation.
"""
Python language provides a built-in function open() to open a file. Following is the
syntax of the function.

open(filename, [mode, [[encoding]] ])

This function, by default opens a file in text and read-only mode.
On success, the function returns a "file" object. Defined in the io module
File object provides the relevant APIs for file manipulation

Throws FileNotFoundError when the file is not found
Throws PermissionError when you do not have the required permission to open a file
Write operation on read-only file throws io.UnsupportedOperation error

Use encoding to open a file in a particular format. cp1252, is the default format on Windows. 
UTF-8 supports Unicode characters
"""

# File close operation
"""
The file object, which we get when a file opens successfully, provides the close().
When a file is closed, it flushes the data from memory to file and closes it.
It is important to close the file after using it.
It is possible to edit a file only when it is open exclusively in write mode by a program. 
So if you leave files open, it may hinder the write operation(s).
"""

# File Open and close operation

# fHandle = open(".\\files\\sample.txt")
# print(fHandle)
# fHandle.close()


# FileNotFoundError: [Errno 2] No such file or directory:
# fHandle = open(".\\files\\sampleee.txt")  # Incorrect file name


# Context manager
"""
Context manager is a feature in Python that allows to manage resources like files, 
database connections, ports, network connections, etc.
When we allocate a resource using a context manager, it automatically releases the resource when 
it is not needed. 
In case of file operation, we use context manager to open a file. And when we are done using 
the file, it automatically closes the file. 
Programmer does not have to close the file explicitly.
"""

# fHandle = open(".\\files\\sample.txt")
# print(fHandle)
# fHandle.close()


# File Open and close operation - Using conext manager
# with open(".\\files\\sample.txt") as fHandle:
#     print(fHandle)


# File open modes.
"""
Since I am covering the text files, I will share the file open modes for text file(s)
Mode	Description
r	    Read only mode. Default mode. File objects positions at the beginning
r+		Read and write mode. File objects positions at the beginning
w		Write mode. Overwrites an existing file. Creates a new one if it does not exist
w+		Write and read mode. Overwrites an existing file. Creates a new one if it does not exist
a		Append mode. File objects positions at the end when file exists. Creates a new one if it 
        does not exist
a+		Append and read mode. File objects positions at the end when file exists. Creates a new 
        one if it does not exist
"""

# File read operations.
"""
read(size)
Reads data and returns a string object when a file is open in text mode
When size is mentioned, it reads size characters from a file
When size is not mentioned or is negative, the whole file is read
During the read operation, the File object position moves ahead of the number of characters read
When data is read beyond the end of a file, returns an empty string

Use the read function when you need to work on a complete file in one go. 
For example, you want to search for a certain pattern in a file.
Use this function with small size files. File read in one go may slow down the program. 
"""

# File read operations - read() - read complete file.
# with open(".\\files\\sample.txt") as fHandle:
#     data = fHandle.read()
#
# print(type(data))
# print(data)


# File read operations - read() - read 50 characters at a time.
# with open(".\\files\\sample.txt") as fHandle:
#     data1 = fHandle.read(50)
#     data2 = fHandle.read(50)
#
# print("data1 = ", data1)
# print("data2 = ", data2)


# File read operations - read() - read data beyond EOF
# with open(".\\files\\sample.txt") as fHandle:
#     data1 = fHandle.read()  # read complete file.
#     data2 = fHandle.read(50)
#
# print("data2 = ", data2)  # this is an empty string


# File read operations.
"""
readline(size) 
Reads a line till it finds a newline (\n) character or End of file (EOF) for the last row
Returns a string when the file is open in text mode
When read beyond the end of the file, returns an empty string
When size is mentioned, reads the size characters from a file or till the newline (\n) character
whichever comes first.

When you use the function to read a complete line, the newline character (\n) is part of 
the data read. So when you print the data, it shows an extra line. In order to remove 
this use the following code 
line = line.strip()
"""

# File read operations - readline() - read a complete line
# with open(".\\files\\sample1.txt") as fHandle:
#     line1 = fHandle.readline()
#     line2 = fHandle.readline()
# print("line1 = ", line1.strip())
# print("line2 = ", line2.strip())


# File read operations - readline() - read few characters
# with open(".\\files\\sample2.txt") as fHandle:
#     line1 = fHandle.readline(200)
#     line2 = fHandle.readline()
# print("line1 = ", line1)
# print("line2 = ", line2)


# File read operations.
"""
readlines(size)
Reads the complete file till EOF is reached
Returns a list of rows read
When size is mentioned (bytes), reads till the end of the line when the bytes are read
"""

# File read operations - readlines() - read complete file
# with open(".\\files\\sample2.txt") as fHandle:
#     lines = fHandle.readlines(60)
#
# for line in lines:
#     line = line.strip()
#     print(line)


# File Pointer.
"""
A marker that indicates the current position within an open file
This marker is used to track the next read or write operation
When a file opens in read (r, r+) or write (w, w+) mode, the marker is at the beginning
When a file opens in append mode (a, a+) mode, the marker is at the end of the file.
Method tell() shares the position of a marker

Method seek(offset, whence)
    Updates files marker position from whence
    Values of whence  are
        0 - from the beginning of the file
        1 - from the current position
        2 - from the end of the file
This function does not do relative seek from the current position and end of the file
"""

# File pointer operations - file open in read mode
# with open(".\\files\\sample2.txt") as fHandle:
#     print(f"tell() at beginning - {fHandle.tell()}")
#     fHandle.readline()
#     print(f"tell() after reading a line - {fHandle.tell()}")


# File pointer operations - file open in read mode
# with open(".\\files\\sample2.txt") as fHandle:
#     print(f"tell at beginning - {fHandle.tell()}")
#     fHandle.seek(31, 0)
#     print(f"tell after 31 char seek op - {fHandle.tell()}")
#     print(fHandle.readline())


# File pointer operations - file open in read mode
# with open(".\\files\\sample2.txt") as fHandle:
#     print(f"tell at beginning - {fHandle.tell()}")
#     fHandle.seek(50, 0)
#     print(f"tell after 50 char seek op - {fHandle.tell()}")

# io.UnsupportedOperation: can't do nonzero cur-relative seeks
#     fHandle.seek(20, 1)  # Operation not allowed

# io.UnsupportedOperation: can't do nonzero end-relative seeks
#     fHandle.seek(20, 2)  # Operation not allowed

# io.UnsupportedOperation: can't do nonzero end-relative seeks
#     fHandle.read()  # go to the end of file
# fHandle.seek(20, 2)


# File write operations
"""
When a file is open in r+ mode, it is open for reading and writing.
The file pointer points at the beginning of the file. 
If the file does not exist, it throws an error.

When a file is open in w or w+ mode, it overwrites the existing file. 
If the mentioned file does not exist, a new blank file is created. 
The marker is positioned at the beginning of a file.

When a file is open in a or a+ mode, it opens the existing file.
If the mentioned file does not exist, a new file is created. 
The marker is positioned at the end of a file.

When we add + to the mode, it means the file is open both in read and write mode.
If you try to read a file open in write mode, it will throw an error.
Write operation starts from where the marker is. 
"""

# File write operations
"""
write(str) - writes the string to a file and returns the number of characters. 

writelines(sequence) - writes a sequence of strings to a file.

While writing the data, the functions write data to an internal buffer. Once the buffer 
is full the content is written to the file. 
If you wish to push the content immediately to a file then use the flush() or close the file.
"""

# File write operations - Open new file in r+ mode, throws an error. File must exist
# with open(".\\files\\a_new_file.txt", "r+") as fHandle:
#     fHandle.write("Hey There")


# File write operation - create new file or empty existing file
# lines = ['\nThis is the first string',
#          '\nThis is the second string',
#          '\nThis is the third string',
#          '\nThis is the fourth string',
#          '\nThis is the fifth string']
#
# with open(".\\files\\new_file.txt", "w+") as fHandle:
#     fHandle.write("Welcome to In Computing World")  # Write at the beginning
#
#     fHandle.writelines(lines)
#     fHandle.write("\nWelcome again to In Computing World")  # Write at the end
#     fHandle.seek(0,0)  # go to the beginning of a file.
#     read_lines = fHandle.read()
# print(read_lines)


# File write operation - open existing file.
# with open(".\\files\\new_file.txt", "r+") as fHandle:
#     fHandle.write("Overwrite first line")  # Write at the beginning
#     fHandle.seek(0, 2)  # go to the end of a file.
#     fHandle.write("\nThis is a new line.")  # Write at the end
#     fHandle.seek(0, 0)  # go to the beginning of a file.
#     read_lines = fHandle.read()
# print(read_lines)


# File write operation - open existing file in a+ mode
lines = ['\nThis is the sixth string',
         '\nThis is the seventh string',
         '\nThis is the eighth string']

with open(".\\files\\new_file.txt", "a+") as fHandle:
    fHandle.writelines(lines)
    fHandle.write("\nNow this is the last line")  # Write at the end
    fHandle.flush()
    fHandle.seek(0, 0)  # go to the beginning of a file.
    read_lines = fHandle.read()
print(read_lines)






