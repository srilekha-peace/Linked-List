class Node:
    def __init__(self, data):
        self.dfield = data
        self.afield = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.afield = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.dfield, end = " ")
            temp = temp.afield

    def reverse_func(self):
        current = self.head
        prev = None
        next = None

        while(current != None):
            next = current.afield
            current.afield = prev
            prev  = current
            current = next

        self.head = prev


l1 = Linkedlist()
l1.insert(50)
l1.insert(40)
l1.insert(30)
l1.insert(20)
l1.insert(10)
print("The given Linkedlist:")
l1.print_list()
l1.reverse_func()
print("\n")
print("The reversed linkedlist:")
l1.print_list()
