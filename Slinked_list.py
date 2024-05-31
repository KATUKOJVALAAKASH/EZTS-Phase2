#linkedlist using recurssion print alternate nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def alt(self):
        def alte_recursive(node, position):
            if node is None:
                return
            if position % 2 == 0:
                print(node.data)
            alte_recursive(node.next, position + 1)

        alte_recursive(self.head, 0)


ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(32)
ll.insert(4)
ll.insert(56)
ll.insert(6)
ll.insert(79)
ll.insert(8)

print("Alternate Values")
ll.alt()