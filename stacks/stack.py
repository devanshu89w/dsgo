class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        # check for valid input
        if value is None:
            raise ValueError("Invalid Value")
        new_node = Node(value)

        if self.top is None:
            self.top = new_node
            self.bottom = self.top
        else:
            new_node.next = self.top
            self.top  = new_node
        self.length += 1
        return self

    def peek(self):
        data_in_top = None
        if self.length == 0:
            return data_in_top
        if self.top is not None:
            data_in_top = self.top.value
        return data_in_top

    def pop(self):
        data = None
        if self.top is not None:
            data_to_pop = self.top
            self.top = self.top.next
            data = data_to_pop.value
            del data_to_pop
        return data

    def __str__(self):
        data = []
        node = self.top
        while node is not None:
            data.append(node.value)
            node = node.next
        return str(data)
