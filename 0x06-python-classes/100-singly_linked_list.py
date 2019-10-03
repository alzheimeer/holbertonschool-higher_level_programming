#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        actual = self.__head
        previo = None
        temp = Node(value)

        if actual is None:
            temp.__next_node = None
            self.__head = temp

        else:
            while actual is not None and value > actual.data:
                previo = actual
                actual = actual.__next_node
            if previo is None:
                temp.__next_node = self.__head
                self.__head = temp
            else:
                previo.__next_node = temp
                temp.__next_node = actual

    def __str__(self):

        n = []
        temp = self.__head
        while temp is not None:
            n.append(str(temp.data))
            temp = temp.__next_node
        return ('\n'.join(n))
