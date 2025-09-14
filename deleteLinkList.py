class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.n = 0
    
    def insert_from_head(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node
        self.n += 1
    
    def __str__(self):
        result = ""
        current = self.head
        if self.head == None:
            result = "[]"
            return result

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
    
    def insert_after(self, after, value):
        new_node = Node(value)
        current = self.head
        while current:
            if after == current.data:
                break
            current = current.next

        if current != None:
            new_node.next = current.next
            current.next = new_node
            self.n += 1
        else:
            print("Item not found")
    
    def clear(self):
        self.head = None
        self.n = 0
    
    def delete_from_head(self):
        if self.head == None:
            return print("Empty LL")
        self.head = self.head.next
        self.n -= 1
    
    def delete_from_tail_pop(self):
        if self.head == None: 
            return print("Empty LL")
        current = self.head
        
        if current.next == None:
            self.delete_from_head()
            return
        
        while current.next.next != None:
            current = current.next
        
        current.next = None
        self.n -= 1
        

L = LinkedList()

L.append(1)
L.append(2)
L.append(3)
L.append(4)

print(L)
L.insert_after(3, 45)
print(L)
L.delete_from_tail_pop()
L.delete_from_tail_pop()
L.delete_from_tail_pop()
L.delete_from_tail_pop()
L.delete_from_tail_pop()
L.delete_from_tail_pop()
print(L)