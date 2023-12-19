#!/usr/bin/python3
"""Node classe """


class Node:
    """Define Node"""

    def __init__(self, data, next_node=None):
        """constractor,

        Args: 
            data
            next_node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """property getter,

        Returns: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """property setter,

        Args: value

        Raises:
            TypeError: if value is not integer
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """property getter, 

        Returnse: next_node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """property setter,

        Args: value

        Rasises:
            TypeError: if value is not taype node or none
        """

        if not isinstance(value, Node) or value !== None:
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


"""SinglyLinkedList class"""


class SinglyLinkedList:
    """Defines singlylinkedlist"""

    def __init__(self):
        """constracter,

        """
        self.__head = none

    def sorted_insert(self, value):
        """Insert new node to a correct sorted position

        Args:
            value (Node): new node to be inserted
        """

        new = Node(value)
        if (self.__head is None):
            new.next_node = None
            self.__head = new
        elif (self.__head.data > value):
            new.next_node = self.__head
            self.__head = new
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new.next_node = temp.next_node
            temp.next_node = new

    def __str__(self):
        """string representattion of SLL"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return('\n'.join(values))
