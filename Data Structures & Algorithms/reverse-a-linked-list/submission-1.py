# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head) :
        old = None
        curr  = head
        while curr!= None:
            temp = curr.next
            curr.next = old
            old = curr
            curr = temp
        return old 
    
            