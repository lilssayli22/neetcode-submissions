# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        b = ListNode(0,None)
        curr = b
        reste = 0
        while l1 and l2 : 
            x = l1.val + l2.val+reste
            if x >=10:
                    a = x-10
                    reste =1
            else :
                    a = x
                    reste =0
            curr.next = ListNode(a,None)
            curr = curr.next
            l1= l1.next
            l2 = l2.next
        if l1 == None :
            while l2!=None:
                x = l2.val+reste
                if x >=10:
                    a = x-10
                    reste =1
                else :
                    a = x
                    reste =0
                curr.next = ListNode(a,None)
                curr = curr.next
                l2 = l2.next
        else :
            while l1!=None:
                x = l1.val+reste
                if x >=10:
                    a = x-10
                    reste =1
                else :
                    a = x
                    reste =0
                curr.next = ListNode(a,None)
                curr = curr.next
                l1 = l1.next
        if reste ==1 :
            curr.next  = ListNode(reste,None)
        return b.next            