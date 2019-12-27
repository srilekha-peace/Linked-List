class Node:
    def __init__(self,key):
        self.data = key
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = Node(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is Empty!!!")
            return
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def rotate(self, R):
        if R == 0:
            return
        temp = self.head
        count = 1
        while count < R and temp is not None:
            temp = temp.next
            count += 1

        if temp is None:
            return

        Kth_Node = temp

        while temp.next is not None:
            temp = temp.next

        temp.next = self.head
        self.head = Kth_Node.next
        Kth_Node.next = None

ll = Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)
ll.append(70)
print("Given Linked list")
ll.print_list()
print("\n")
ll.rotate(4)
print("Rotated by R times - Linkedlist")
ll.print_list()
