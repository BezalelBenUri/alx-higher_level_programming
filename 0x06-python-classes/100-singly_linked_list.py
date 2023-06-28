#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Class that defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a Node instance with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data attribute"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list"""

    def __init__(self):
        """Initializes a SinglyLinkedList instance"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and\
                    value >= current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the SinglyLinkedList"""
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)
