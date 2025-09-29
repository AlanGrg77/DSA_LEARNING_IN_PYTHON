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
            data = self.top.data #Assign and save the data first before we pop it so that we know which item we are poping, can't do it after sel.top =self.top.next becuase we will lose the data we are poping and also if its last element then the next data will be null or None
            self.top = self.top.next
            
        return data
    
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
    
    def reverse(self, text):
        s = Stack()
        for i in text:
            s.push(i)
        
        result = ''

        while not s.isEmpty():
            result = result + s.pop()
        
        return print(result)


    
S = Stack()
S.push(1)
S.push(2)
S.push(3)

S.traversal()
S.bottom()
S.peek()
S.reverse("Hello")