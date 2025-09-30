#Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.



class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self,val):
        new_node = ListNode(val)
        current = self.head
        if current == None:
            self.head = new_node
            return
        while current.next:
            current = current.next

        current.next = new_node 
    def __str__(self):
            curr = self.head
            result = ''

            while curr != None:
                result = result + str(curr.val) + "->"
                curr = curr.next
            return result[:-2]   

class Solution:
    def addTwoNumbers(self,l1,l2):
        dummy = ListNode() # create a dummy node and first node is dummy(0) so discard it and just use it to add new created nodes
        current = dummy # use as pointer insetad of knowing the exact head we take dummy as head
        carry = 0

        while l1 or l2 or carry: # here carray is also needed to be not None becaue its an edge case where 7+8 at the end will give a carry and we need to stoe the carry as a node as well
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_val = v1 + v2 + carry
            carry = sum_val // 10 # if 15 is sum then carry will be 1 here
            digit = sum_val % 10 # digigt is the value that we store in node and if 15 sum then digit is 5 here

            current.next = ListNode(digit) # now the actual node that are added are our result
            current = current.next #move to next node but oder matter, add node irst and only then moving current tot current.next

            if l1 : l1 = l1.next # if l1 exits then move to next index
            if l2 : l2 = l2.next # if l2 exits then move to next index

        return dummy.next # return dummy.next because dummy has not needed inital data of dummy(0) like "dummy(0) -> 1 ->2 ->3" so just reyurn from next ie 2nd index 1 -> 2...
     
    
L1 = LinkedList()
L1.append(1)
L1.append(2)
L1.append(3)
L1.append(4)
print(L1)

L2 = LinkedList()
L2.append(2)
L2.append(5)
L2.append(6)
print(L2)

s = Solution()
result_head = s.addTwoNumbers(L1.head, L2.head)  # pass head nodes

# Convert result to readable string
result_list = []
while result_head:
    result_list.append(str(result_head.val))
    result_head = result_head.next

print("Result:", "->".join(result_list))