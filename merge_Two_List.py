class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class List1:

    def __init__(self):
        self.head = None
        self.n = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head ==  None:
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

class List2:

    def __init__(self):
        self.head = None
        self.n = 0
    
    def append(self, value):
        new_node = Node(value)
        if self.head ==  None:
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
class MergeSolution:

    def __init__(self):
        self.head = None
        self.n = 0
    
    def merge(self, list1, list2):
        new_node = Node(-1)
        current = new_node

        while list1 and list2:
            if list1.data <= list2.data:
                current.next = list1 
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        self.head = new_node.next
        return self.head
    
    def __str__(self):
        current = self.head
        result = ""
        while current:
            result = result + str(current.data) + "->"
            current = current.next
        result += "null"
        return result
    

# Create the first linked list
list1 = List1()
list1.append(1)
list1.append(3)
list1.append(5)
print("List1:", list1)

# Create the second linked list
list2 = List2()
list2.append(2)
list2.append(4)
list2.append(6)
print("List2:", list2)

# Merge the two lists
merger = MergeSolution()
# The merge method expects the head nodes of the lists
merged_head = merger.merge(list1.head, list2.head)


print(merger)
