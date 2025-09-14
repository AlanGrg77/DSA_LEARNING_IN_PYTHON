class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class LinkedList:
        
        def __init__(self):
            self.head = None #Empty list
            self.n = 0       #Number of nodes

        def __len__(self):
            return self.n

        def insert_head(self,value):
            new_node = Node(value) #new node
            new_node.next = self.head #create connection
            self.head = new_node   #reassign head
             
            self.n += 1
        def traverse(self):
            current = self.head
            while current != None:
                  print(current.data, end="->")
                  current = current.next

            print("null")

        def __str__(self):
            curr = self.head
            result = ''

            while curr != None:
                result = result + str(curr.data) + "->"
                curr = curr.next
            return result[:-2]
        
        def append(self,value):
            new_node = Node(value)

            if self.head == None:
                 self.head = new_node
                 self.n += 1
                 return

            curr = self.head

            while curr.next: 
                 curr = curr.next
            
            #you are at last node
            curr.next = new_node
            self.n += 1 

L = LinkedList()

L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)


L.traverse()

print(L)
L.append(7)
print(L)