def sc2_func1():
    print("script2.py is running as main file. Scope of this file is the global scope.")


def sc2_func2():
    print(f"Function sc2_func2 from script2.py is called")


_test = "test string"

my_list = [11, 12, 13]

print(f"Script2 - __name__ == {__name__}")
if __name__ == "__main__":
    sc2_func1()
    print(dir())  # shows names of objects in present namespace (global in this case)
else:
    print("Script2.py is being imported in another module")
