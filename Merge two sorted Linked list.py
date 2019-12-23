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

def merge_list(head1,head2):
    dummy_node = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.dfield < head2.dfield:
        dummy_node = head1
        dummy_node.afield = merge_list(head1.afield, head2)
    else:
        dummy_node = head2
        dummy_node.afield = merge_list(head1,head2.afield)

    return dummy_node

l1 = Linkedlist()
l1.insert(55)
l1.insert(40)
l1.insert(37)
l1.insert(25)
l1.insert(15)
l1.insert(5)

l2 = Linkedlist()
l2.insert(50)
l2.insert(45)
l2.insert(30)
l2.insert(20)
l2.insert(10)
l2.insert(1)

list3 = Linkedlist()
list3.head = merge_list(l1.head, l2.head)
list3.print_list()
