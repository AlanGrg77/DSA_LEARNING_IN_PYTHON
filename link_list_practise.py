class Node:
    
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None # The linked list is considered empty if its none
        self.n = 0

    def preppend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        current = self.head
        result = ""
        while current:
            result = result + str(current.data) + "->" 
            current = current.next
        return result[:-2]
    
    def append(self, value):
        new_node = Node(value)

        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
        self.n += 1


L = LinkedList()

L.append(1)
L.append(2)
L.append(3)
L.append(4)
L.preppend(0)

print(L)