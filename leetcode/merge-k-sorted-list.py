# Definition for singly-linked list.
from heapq import heappush, heappop
from typing import List

class MyList:
     def __init__(self, x: ListNode):
         self.listNode = x
     def __eq__(self, other):
         return self.listNode.val == other.listNode.val
     def __lt__(self, other):
         return self.listNode.val < other.listNode.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heapq = []
        for listNode in lists:
            if listNode:
                heappush(heapq, MyList(listNode))

        pointer = None
        theHead = None

        while heapq:
            myList = heappop(heapq)
            if theHead == None:
                pointer = ListNode(myList.listNode.val)
                theHead = pointer
            else:
                pointer.next = ListNode(myList.listNode.val)
                pointer = pointer.next

            if myList.listNode.next:
                heappush(heapq, MyList(myList.listNode.next))

        return theHead
