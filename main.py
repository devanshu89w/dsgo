from hashtables.hash_table import  HashTable
from linkedlist.linked_list import LinkedList
from stacks.stack import Stack
from bst.binary_search_tree import BinarySearchTree
from bst.binary_search_tree import traverse


if __name__ == "__main__":
    # DS - HashTable
    # h_table = HashTable(size=5)
    # print(h_table)
    # h_table.set("apples", 1000)
    # print(h_table)

    # DS - Linked List
    # my_list = LinkedList()
    # print(my_list)
    # my_list.append(10)
    # print(my_list)
    # my_list.append(20)
    # my_list.append(30)
    # my_list.append(40)
    # my_list.append(50)
    # print(my_list)
    # my_list.prepend(0)
    # print(my_list)
    # my_list.insert(3, 25)
    # print(my_list)
    # my_list.remove(3)
    # print(my_list)

    # DS - Stack
    # stck = Stack()
    # stck.push("10")
    # stck.push("20")
    # stck.push("30")
    # print(stck)
    # stck.pop()
    # stck.pop()
    # stck.pop()
    # stck.pop()
    # print(stck)
    # print(stck.peek())

    # print([10, 20].pop())

    # DS - Binary Search Tree
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(8)
    bst.insert(11)
    bst.insert(5)
    bst.insert(1)
    bst.insert(21)
    bst.insert(31)
    print(traverse(bst.root))

