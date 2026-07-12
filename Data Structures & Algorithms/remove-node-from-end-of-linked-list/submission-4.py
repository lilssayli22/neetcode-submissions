class Solution:
    def removeNthFromEnd(self, head, n: int):
        n0 = 0
        a = head
        while a:
            n0 += 1
            a = a.next
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        i = 1
        while i != n0 - n + 1:
            prev = curr
            curr = curr.next
            i += 1
        
        prev.next = curr.next
        return dummy.next