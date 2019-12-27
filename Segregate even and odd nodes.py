class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp =self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def segregate_func(self,list):
        evenstart = None
        evenend = None
        oddstart = None
        oddend = None
        temp = list

        while temp:
            var = temp.data
            if var % 2 == 0:
                if evenstart is None:
                    evenstart = temp
                    evenend = evenstart
                else:
                    evenend.next = temp
                    evenend = evenend.next
            else:
                if oddstart is None:
                    oddstart = temp
                    oddend = oddstart
                else:
                    oddend.next = temp
                    oddend = oddend.next
            temp = temp.next

        if evenstart != None:
            list = evenstart

        if evenend != None:
            evenend.next = oddstart

        if oddend != None:
            oddend.next = None

        return list


ll = Linkedlist()
ll.append(10)
ll.append(5)
ll.append(15)
ll.append(20)
ll.append(30)
ll.append(45)
ll.append(1)
ll.head = ll.segregate_func(ll.head)
ll.print_list()
