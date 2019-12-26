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

    def reverse(self, list):
        if list is None:
            return
        next = None
        prev = None
        while list is not None:
            next = list.next
            list.next = prev
            prev = list
            list = next
        list = prev
        return list

    def middle(self,list):
        if list is None:
            return
        slow = list
        fast = list
        while (fast.next != None) and (fast.next.next != None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def identical(self, l1, l2):
        if l1 is None or l2 is None:
            return False
        if l1 is None and l2 is None:
            return True
        while l1 != None and l2 != None:
            if l1.dfield != l2.dfield:
                return False
            l1 = l1.next
            l2 = l2.next
        return True

    def palindrome(self,list):
        if list is None:
            print("List is empty")
        middle_e = self.middle(list)
        nexttomiddle = middle_e.next
        middle_e.next = None
        l1 = list
        l2 = self.reverse(nexttomiddle)
        check_func = self.identical(l1,l2)
        if check_func is True:
            print("Palindrome")
        else:
            print("Not a Palindrome")

ll = Linkedlist()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
ll.append("C")
ll.append("B")
ll.append("A")
ll.head = ll.palindrome(ll.head)
