class Node:
    def __init__(self, data):
        self.dfield = data
        self.afield = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node =Node(data)
        if self.head is None:
            self.head = new_node
            return

        new_node.afield = self.head
        self.head = new_node

    def print_list(self):
        temp =self.head
        while temp is not None:
            print(temp.dfield, end = " ")
            temp = temp.afield

    def sort(self):
        count = [0,0,0]
        temp =self.head

        while temp is not None:
            count[temp.dfield] += 1
            temp = temp.afield

        i = 0
        temp = self.head

        while temp is not None:
            if count[i] == 0:
                i += 1
            else:
                temp.dfield = i
                count[i] -= 1
                temp = temp.afield

l1 = Linkedlist()
l1.insert(1)
l1.insert(2)
l1.insert(0)
l1.insert(1)
l1.insert(1)
l1.insert(2)
l1.insert(0)
l1.insert(1)
l1.insert(2)
l1.insert(1)
l1.insert(0)
l1.sort()
l1.print_list()


