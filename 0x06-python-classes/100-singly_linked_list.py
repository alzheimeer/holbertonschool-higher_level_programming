#!/usr/bin/python3
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        if value is None or isinstance(value, Node):
            self.__next = value
        else:
            raise TypeError("next must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        actual = self.__head
        previo = None
        temp = Node(value)

        if actual is None:
            temp.__next = None
            self.__head = temp

        else:
            while actual is not None and value > actual.data:
                previo = actual
                actual = actual.__next
            if previo is None:
                temp.__next = self.__head
                self.__head = temp
            else:
                previo.__next = temp
                temp.__next = actual

    def __str__(self):

        n = []
        temp = self.__head
        while temp is not None:
            n.append(str(temp.data))
            temp = temp.__next
        return ('\n'.join(n))
