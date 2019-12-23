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

    def identical_func(self, other):
        list1 = self.head
        list2 = other.head

        if list1 is None or list2 is None:
            print("Lists are not Identical")

        if list1 is None and list2 is None:
            print("Lists are Identical")

        while (list1 != None) and (list2 != None):
            if list1.dfield != list2.dfield:
                print("Lists are not Identical")
                return
            list1 = list1.afield
            list2 = list2.afield

        print("Lists are Identical")

l1 = Linkedlist()
l1.insert("F")
l1.insert("E")
l1.insert("D")
l1.insert("C")
l1.insert("B")
l1.insert("A")

l2 = Linkedlist()
l2.insert("F")
l2.insert("E")
l2.insert("D")
l2.insert("C")
l2.insert("B")
l2.insert("A")

l1.identical_func(l2)
