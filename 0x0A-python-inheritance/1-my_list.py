#!/usr/bin/python3


class MyList(list):
    """class that inherit from list"""
    def print_sorted(self):
        """Prints the sorted list"""
        print(set(self))
