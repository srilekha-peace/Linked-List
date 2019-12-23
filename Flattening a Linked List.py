class Node:
    def __init__(self,data):
        self.dfield = data
        self.right = None
        self.down = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.dfield, end = " ")
            temp = temp.down

def merge_list(head1,head2):
    dummy_node = None

    if head1 is None:
        return head2

    if head2 is None:
        return head1

    if head1.dfield < head2.dfield:
        dummy_node = head1
        dummy_node.down = merge_list(head1.down, head2)
    else:
        dummy_node = head2
        dummy_node.down = merge_list(head1,head2.down)

    return dummy_node

def flatten(root):
    if root is None or root.right is None:
        return root

    return merge_list(root, flatten(root.right))

l1 = Linkedlist()
l1.head = Node(4)
l1.head.down = Node(5)
l1.head.down.down = Node(8)
l1.head.down.down.down = Node(10)
l1.head.right = Node(7)
l1.head.right.down = Node(9)
l1.head.right.down.down = Node(25)
l1.head.right.right = Node(11)
l1.head.right.right.down = Node(13)
l1.head.right.right.down = Node(22)

list2 = Linkedlist()
list2.head = flatten(l1.head)
list2.print_list()
