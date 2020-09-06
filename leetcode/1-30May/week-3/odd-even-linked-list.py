# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

objHead = ListNode(0)
obj1 = ListNode(1)
obj2 = ListNode(2)

objHead.next = obj1
objHead.next.next = obj2
print(obj1.next.val)
