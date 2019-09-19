# 0x04. Python - More Data Structures: Set, Dictionary
## OBJECTIVES
how to use sets
when to use sets versus lists
how to use dictionaries
how to iterate into a dictionary
how to use lambda functions
how to use map and reduce functions
## REQUIREMENTS 

the first line of all files should be exactly #!/usr/bin/python3
all code should use the PEP8 style (version 1.7.*)
all files must be executable
all files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
# EXERCISES
## MANDATORY
**0-square_matrix_simple.py** - Computes the square value of all integers in a matrix
Prototype: def square_matrix_simple(matrix=[]):

**1-search_replace.py**- Replaces all occurences of a specific element with a different element in a new list
Prototype: def search_replace(my_list, search, replace):

**2-uniq_add.py** - Finds the sum of all unique integers in a list
Prototype: def uniq_add(my_list=[]):

**3-common_elements.py** - Returns a set of common elements in two sets
Prototype: def common_elements(set_1, set_2):

**4-only_diff_elements.py** - Returns a set of elements only present in one of two sets
Prototype: def only_diff_elements(set_1, set_2):

**5-number_keys.py** - Returns the number of keys in a dictionary
Prototype: def number_keys(a_dictionary):

**6-print_sorted_dictionary.py** - Prints a dictionary by ordered keys
Prototype: def print_sorted_dictionary(a_dictionary):

**7-update_dictionary.py** - Replaces or adds a key to a dictionary
Prototype: def update_dictionary(a_dictionary, key, value):

**8-simple_delete.py** - Deletes a key in a dictionary
Prototype: def simple_delete(a_dictionary, key=""):

**9-multiply_by_2.py** - Returns a new dictionary where all original integers have been multiplied by 2
Prototype: def multiply_by_2(a_dictionary):

**10-best_score.py **- Returns a key with the biggest integer value
Prototype: def best_score(a_dictionary):

**11-mutiply_list_map.py** - Returns a list with all values multiplied by a number without using any loops.
Prototype: def mutiply_list_map(my_list=[], number=0):

**12-roman_to_int.py** - Converts a Roman numeral to an integer
Prototype: def roman_to_int(roman_string):

ADVANCED
100-weight_average.py - Returns the weighted average of all integers tuple (<score>, <weight>)
Prototype: def weight_average(my_list=[]):

101-square_matrix_map.py - Computes the square value of all integers of a matrix using map
Prototype: def square_matrix_map(matrix=[]):

102-complex_delete.py - Deletes keys with a specific value in a dictionary
Prototype: def complex_delete(a_dictionary, value):

103-python.c - Create two C functions that print some basic info about Python lists and Python bytes objects.
Prototypes: void print_python_list(PyObject *p);, void print_python_bytes(PyObject *p);