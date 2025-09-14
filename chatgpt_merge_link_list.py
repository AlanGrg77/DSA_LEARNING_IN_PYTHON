class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def __str__(self):
        result = []
        curr = self.head
        while curr:
            result.append(str(curr.data))
            curr = curr.next
        return "->".join(result) + "->null"


def merge_sorted_lists(l1, l2):
    """Merge two sorted linked lists and return a new LinkedList"""
    dummy = Node(-1)   # dummy node for simplicity
    tail = dummy

    # Merge step (like in merge sort)
    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append leftovers
    tail.next = l1 if l1 else l2

    # Create a merged LinkedList
    merged = LinkedList()
    merged.head = dummy.next
    return merged


# ---- Example Run ----
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

print("List1:", list1)
print("List2:", list2)

merged_list = merge_sorted_lists(list1.head, list2.head)
print("Merged :", merged_list)
