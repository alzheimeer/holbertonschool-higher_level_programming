#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.__data = data

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
        if value  == None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):

        if not isinstance(value, int):
            raise TypeError("data must be an integer")


        aux = None
        i = self.__head
        new_node = Node(value)

        if self.__head is None:
            new_node.__next_node = None
            self.__head = new_node

        else:
            while i is not None and value > i.data:
                aux = i
                i = i.__next_node
            if aux is None:
                new_node.__next_node = self.__head
                self.__head = new_node
            else:
                aux.__next_node = new_node
                new_node.__next_node = i

    def __str__(self):

        list1 = []
        while self.__head is not None:
            list1.append(self.__head.data)
            self.__head = self.__head.__next_node
        return ('\n'.join(str(self.__head) for self.__head in list1))
