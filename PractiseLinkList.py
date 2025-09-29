class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
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
        result = ""
        current = self.head
        if self.head == None:
            return print("[]")

        while current:
            result = result + str(current.data) + "->"
            current = current.next
        
        return result[:-2]
    
    def delete_from_head(self):
        if self.head == None:
            return print("Empty LL")
        self.head = self.head.next


    def delete_from_tail(self):
        if self.head == None:
            return print("Empty LL")
         
        current = self.head

        while current.next.next:
            current = current.next
        
        if current is not None:
            current.next = None  
    def delete_by_index(self, index):
        if self.head == None:
            return print("Empty LL")
        
        if index == 0:
            self.head = self.head.next
            return 
        
        current = self.head
        pos = 0
        while current.next:
            if pos == index:
                break
            current = current.next
            pos += 1

        if current is not None:
            current.next = current.next.next
        else:
            print("index not found")

    def insert(self, value, position):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        pos = 0

        while current:
            if position == pos:
                 break
            current = current.next
            pos += 1

        if current is not None:
            new_node.next = current.next
            current.next = new_node
        else:
            return print("index not in LL")

    def search_by_index(self, index):
        pos = 0
        current = self.head

        while current:
            if pos == index:
                return print("value: ", current.data)
            current = current.next
            pos += 1


    
L = LinkedList()

L.append(1)
L.append(2)
L.append(3)
L.append(4)


print(L)
L.insert(20, 1)

print(L)

L.search_by_index(2)
L.delete_by_index(2)
print(L)