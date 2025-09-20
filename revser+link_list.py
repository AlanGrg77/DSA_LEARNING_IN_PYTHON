class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None # Empty Linked List
        self.n = 0
    
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
    
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result = result + str(current.data) + "->"
            current = current.next
        return result[:-2]
    def reverse(self):
        prev, current = None, self.head

        while current:
            next_node = current.next #need to do this so that we can keep track of next|_nodes without losing it
            current.next = prev #reverse the arrow or adrees or pointer to previous

            #Shifting the pre,current and next by 1 step
            prev = current
            current = next_node
        self.head = prev
        return self.head



L = LinkedList()
L.append(1)
L.append(2)
L.append(3)
L.append(4)
print(L)


L.reverse()
print(L)

