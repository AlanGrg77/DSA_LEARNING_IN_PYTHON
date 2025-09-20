class Node:

    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:

    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self, value):
        new_node = Node(value)
        
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if(self.isEmpty()):
            return print("Stck is emopty")
        else:
            self.top = self.top.next
    
    def bottom(self):
        current = self.top
        while current.next:
            current = current.next
        result = current.data
        return print("Bottom is", result)
    
    def peek(self):
        if(self.isEmpty()):
            return print("Stack is empty")
        else:
            return print("Peek of stack: ", self.top.data)
    
    def traversal(self):
        current = self.top

        while current:
            print(current.data)
            current = current.next

    
S = Stack()
S.push(1)
S.push(2)
S.push(3)

S.traversal()
S.bottom()
S.peek()