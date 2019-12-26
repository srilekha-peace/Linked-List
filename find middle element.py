class Node:
    def __init__(self,data):
        self.dfield = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("No nodes in the list")
            return
        temp = self.head
        while temp:
            print(temp.dfield, end = " ")
            temp = temp.next

    def middle(self,list):
        if list is None:
            return
        slow = list
        fast = list
        while (fast.next != None) and (fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        print(slow.dfield)


ll = Linkedlist()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.append("E")
ll.append("F")
ll.append("G")
ll.head = ll.middle(ll.head)
