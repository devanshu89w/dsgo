class Node:
    def __init__(self, value):
        # check for valid value
        if value is None:
            raise ValueError("Invalid value for Node")

        self.left = None
        self.right = None
        self.value = value

    def __str__(self):
        import json
        return json.dumps(self.__dict__)
        """"
        return { 
             "node": {
                "left": None,
                "right": None,
                "value": self.value,  # Mistake - again forgot to write self
            }
        }"""


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # check for valid value
        if value is None:
            raise ValueError("Invalid Value")
        # check if root is None, if so add the new node as root,
        # else decide where to add the new node based on the value of the root node and the input value

        new_node = Node(value)  # Mistake - used a hardcoded number should avoid this silly error.

        if self.root is None:
            self.root = new_node
        else:
            # traverse to the left or right
            # if value is less than the value in root, go left else go right
            node = self.root

            while node.left is not None or node.right is not None:
                if node.left is not None and value < node.value:
                    # traverse left
                    node = node.left
                elif node.right is not None and value > node.value:
                    node = node.right
                else:
                    break

            if value < node.value:
                node.left = new_node
            else:
                node.right = new_node
        return self

    def __str__(self):
        import json
        return json.dumps(self.root.__dict__)  # Mistake - dump the dict obj as it is json


"""
9
/		\
8				11
5				10		15
"""


def traverse(node):
    # check for input
    if node is None:
        return {}

    # base case
    if node.left is None and node.right is None:
        return str(node)

    left, right = None, None

    if node.left is not None:
        left = traverse(node.left)
    if node.right is not None:
        right = traverse(node.right)

    return {
        "left": left,
        "right": right,
        "value": node.value,
    }
