#!/usr/bin/python3

"""
This file contain classes and interfaces for dealing with
singly linked lists
"""


class Node:
    """
    defines a node in a linked list
    """

    def __init__(self, data, next_node=None):
        """
        initialize a new node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        retrieve node's data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        sets a node's data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        retrieve node's next
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        set a node's next
        """
        if not isinstance(value, (Node, type(None))):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    interface that represents a singly linked list
    """

    def __init__(self):
        """
        initialize singly linked list
        """
        self.__head = None

    def __str__(self):
        """
        string representation of the linked list
        """
        string = ""
        start = self.__head
        while start:
            if start is not self.__head:
                string += '\n'
            string += str(start.data)
            start = start.next_node
        return string

    def sorted_insert(self, value):
        """
        inserts a new node into the correct sorted
        position in the list
        """
        new = Node(value)

        if not self.__head:
            self.__head = new
            return
        prev = None
        temp = self.__head
        while temp:
            if value < temp.data:
                break
            prev = temp
            temp = temp.next_node
        if prev:
            prev.next_node = new
        else:
            self.__head = new
        new.next_node = temp
