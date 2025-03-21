# Modules and Packages.

"""
import <module_name>

from <module_name> import object1, object2

from <module_name> import *
"""


# Module import best practice
"""
In general, do not use 
    from module import *,
    Clutters name space and makes detection of undefined names difficult

Import modules at top of a file. This gives a clarity on modules being imported
Use one import per line, makes it easy to add / remove imports
Good to import the modules in the following sequence

Standard library modules - sys, os, re, etc
Third party modules
Locally developed modules
"""

# Packages

"""
Package_Folder
    __init__.py
    Sub_package_folder1
        __init__.py
        module3.py
        module1.py # this is possible too.
    Sub_package_folder2
        __init__.py
        module4.py
    module1.py
    module2.py
"""



"""
Pack
    __init__.py
    SubPackage1
        __init__.py
        Module3.py
    SubPackage2
        __init__.py
    Module1.py
    Module2.py
"""












