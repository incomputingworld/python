my_list = [1, 2, 3]


def sc1_func1():
    print("script1.py is running as main file. Scope of this file is the global scope.")


def sc1_func2():
    print(f"Function sc1_func2 from script1.py is called")




print(f"Script1 - __name__ == {__name__}")
if __name__ == "__main__":
    sc1_func1()
    print(dir())  # shows names of objects in present namespace (global in this case)
else:
    print("Script1.py is being imported in another module")

print(my_list)
