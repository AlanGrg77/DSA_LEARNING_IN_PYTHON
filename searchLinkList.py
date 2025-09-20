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

    def delete_by_value(self, value):
        current = self.head

        if self.head == None:
            return print("Empty LL")

        if current.data == value: #or just self.head.data
            self.delete_from_head()
            return

        while current.next:
            if current.next.data == value:
                break
            current = current.next
        
    
        if current.next == None:
            return print("Not found")
        else:
            current.next = current.next.next

    def search(self, target):
        pos = 0
        current = self.head

        while current:
            if current.data == target:
                return print("located in index: ",pos)
            pos +=1
            current = current.next

    def search_by_index(self, targetIndex):
        current = self.head
        pos = 0
        while current:
            if pos == targetIndex:
                return print(f"at index {targetIndex}, value is :", current.data)
            current = current.next
            pos += 1
    def max_in_LL(self):
        if self.head == None:
            return print("Empty LL")
        max = self.head
        current = self.head.next

        while current:
            if current.data > max.data:
                max.data = current.data
            current = current.next
        print("Max value: ", max.data)
    def min_in_LL(self):
        if self.head == None:
            return print("Empty LL")
        min = self.head
        current = self.head.next

        while current:
            if current.data < min.data:
                min.data = current.data
            current = current.next
        print("Min value: ", min.data)
    def replace_max_value(self, value):
        if self.head == None:
            return print("Empty LL")
        max = self.head
        current = self.head.next

        while current:
            if current.data > max.data:
                max.data = current.data
            current = current.next
        
        max.data = value
        print("current LinkedList", self)
        print("Max value", max.data)



L = LinkedList()

L.append(1)
L.append(2)
L.append(3)
L.append(4)

print(L)
L.insert_after(3, 45)
print(L)
L.search_by_index(3)
print(L)
L.max_in_LL()
L.min_in_LL()
L.replace_max_value(9)