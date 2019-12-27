class Node:
    def __init__(self,key):
        self.data = key
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end = " ")
            temp = temp.next

    def middle(self,head):
        if head is None:
            return head
        slow = head
        fast = head

        while (fast.next != None) and (fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, a,b):
        result = None
        if a == None:
            return b
        if b == None:
            return a

        if a.data <= b.data:
            result = a
            result.next =self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a,b.next)
        return result

    def merge_sort(self, h):
        if h is None or h.next  is None:
            return h

        middle_e = self.middle(h)
        next_to_middle = middle_e.next
        middle_e.next = None

        left =self.merge_sort(h)
        right =self.merge_sort(next_to_middle)
        sorted_list = self.sorted_merge(left,right)
        return sorted_list


ll = Linkedlist()
ll.append(10)
ll.append(5)
ll.append(30)
ll.append(20)
ll.append(15)
ll.append(45)
ll.append(1)
ll.head = ll.merge_sort(ll.head)
ll.print_list()
