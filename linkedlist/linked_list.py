from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.__dict__)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        # Mistake : did not check for valid input. should have checked for None
        if value is None:
            raise Exception("invalid value")
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
        elif self.tail is not None:
            new_node = Node(value)
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        return self

    def prepend(self, value):
        # check for valid input
        if value is None:
            raise Exception("Invalid value")
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.length = 1
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def __str__(self):
        # from the head traverse until  we find tail
        data = []
        node = self.head
        # if node is None:
        #    return str(data)  # Mistake - missed explicit string conversion
        while node is not None:  # Mistake - node .next is not fails when length is 1
            data.append(node.value)
            node = node.next
        return str(data)

    def insert(self, index, value):
        # check for valid input; index >=0, value is not None
        if value is None:
            raise Exception("Invalid value")
        if index < 0 and index < self.length:
            raise Exception("Invalid index")
        # get the head node and traverse till the passed index
        node = self.head
        for _ in range(0, index - 1):
            node = node.next


        # idx = 0
        # while node is not None and idx != index - 1:
        #     node = node.next
        #     idx += 1

        new_node = Node(value)
        new_node.next = node.next
        node.next = new_node

        return self

    def remove(self, index):
        # check for valid input; index ≥ 0 and index < length
        if index < 0 and index >= self.length:
            raise Exception("Invalid Input")

        # get the head and go one node less than the one we want to delete
        node = self.head
        for _ in range(0, index-1):
            node = node.next
        node_to_delete = node.next
        node.next = node_to_delete.next
        del node_to_delete
        return self

        # idx = 0
        # while None in Any[self.head, node] and idx != index - 1:
        #     node = node.next
        #     idx += 1
